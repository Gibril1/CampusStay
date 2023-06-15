from .utils import validate_email, validate_phone_number

def validate_registration_data(data):
    response = {
        "data": {},
        "error_message": ""
    }

    if not data['username']:
        response['error_message'] = 'Username has not been provided'
        return response, 400
    if not data['email_address']:
        response['error_message'] = 'Email Address has not been provided'
        return response, 400
    if not validate_email(data['email_address']):
        response['error_message'] = 'Please enter a valid email address'
        return response, 400
    if not data['password']:
        response['error_message'] = 'Password has not been provided'
        return response, 400
    if not data['role']:
        response['error_message'] = 'Role has not been provided'
        return response, 400
    if data['role'] != 'manager' and data['role'] != 'student':
        response['error_message'] = 'Role is either student or manager'
        return response, 400
    if data['role'] == 'student' and not data['reference_number']:
        response['error_message'] = 'Every student must have a reference number'
        return response, 400
    if data['password'] != data['password2']:
        response['error_message'] = 'Passwords do not match'
        return response, 400
    if data['phone_number'] and not validate_phone_number(data['phone_number']):
        response['error_message'] = 'Phone number is invalid'
        return response, 400

    return None  

def validate_login_data(username, password):
    response = {
        "data": {},
        "error_message": ""
    }

    if not password:
        response['error_message'] = 'Password has not been provided'
        return response, 400
    if not username:
        response['error_message'] = 'Username has not been provided'
        return response, 400
    
    return None
