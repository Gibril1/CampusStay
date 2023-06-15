from flask import jsonify, request
from main import bcrypt

from ..utils.user_validations import (
    validate_registration_data, 
    validate_login_data
)
from ..services.user_services import (
    user_exists, 
    create_user, 
    create_student_profile,
    create_hostel_manager_profile
)

from ..serializers.user_serializers import (
    user_schema
)
from ..utils.utils import createJWT

def register_user():
    try:
        response = {
            "data":{},
            "error_message":""
        }
        data = request.json
        
        validation_result = validate_registration_data(data)
        if validation_result is not None:
            return jsonify(validation_result)
      
        # check if user exists
        user = user_exists(data['username'])
        if user:
            response['error_message'] = 'User account already exists.'
            return jsonify(response), 400

        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

        # set user data
        user_data = {
            'username': data['username'],
            'email_address': data['email_address'],
            'role': data['role'],
            'password': hashed_password,
        }

        # create user data
        try:
            user = create_user(user_data)
            user = user_schema.dump(user)
        except Exception as e:
            response['error_message'] = str(e)
            return jsonify(response), 400
        
      
        # create student profile of user
        if user['role'] == 'student':
            # set the student profile data
            student_profile_data = {
                'reference_number':data['reference_number'], 
                'user' : user['id'], 
                'first_name' : data['first_name'], 
                'last_name':data['last_name'], 
                'other_name':data['other_name'], 
                'phone_number' : data['phone_number'], 
                'program_of_study' : data['program_of_study'], 
                'gender' : data['gender']
            }
            try:
                student_profile = create_student_profile(student_profile_data)
            except Exception as e:
                response['error_message'] = e
                return jsonify(response), 400
            response["data"] = 'Account has been successfully created'
            return jsonify(response), 200
        
        # create hostel manager
        elif user['role'] == 'manager':
            # set hostelmanager profile
            hostelmanager_profile = {
                'first_name': data['first_name'],
                'last_name': data['last_name'],
                'other_name': data['other_name'],
                'phone_number': data['phone_number'],
                'gender': data['gender'],
                'user': user['id'],
            }
            try:
                manager = create_hostel_manager_profile(hostelmanager_profile)
            except Exception as e:
                response['error_message'] = str(e)
                print('printing error')
                print(e)
                return jsonify(response), 400
            response['data'] = 'Account has been successfully created'
            return jsonify(response), 200
        else:
            response['error_message'] = 'Invalid credentials'
            return response, 400
    except Exception as e:
        response['error_message'] = str(e)
        return jsonify(response), 500
    

def login_user():
    try:
        response = {
            "data":{},
            "error_message":""
        }

        username = request.json.get('username')
        password = request.json.get('password')

        validation_result = validate_login_data(username, password)
        if validation_result is not None:
            return validation_result

        # check if user exists
        user = user_exists(username)
        if user and bcrypt.check_password_hash(user.password, password):
            token = createJWT(username=user.username)       
            response['data']["auth_token"] = token
            return response, 200
        else:
            response['error_message'] = 'Invalid Credentials/ No such user'
            return response, 404      
    except Exception as e:
        response['error_message'] = str(e)
        return response, 500