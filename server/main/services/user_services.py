from main import db

from main.models.user_models import (
    HostelManager, 
    StudentProfile,  
    User,   
)

def user_exists(username):
    user = User.query.filter_by(username=username).first()
    return user


def create_user(user_data):
    user = User(
        username=user_data['username'], 
        email_address=user_data['email_address'], 
        password=user_data['password'], 
        role=user_data['role']
     )
    db.session.add(user)
    db.session.commit()
    return user

def create_student_profile(data):
    student_profile = StudentProfile(
        reference_number=data['reference_number'], 
        user = data['user'], 
        first_name = data['first_name'], 
        last_name=data['last_name'], 
        other_names=data['other_name'], 
        phone_number = data['phone_number'], 
        program_of_study = data['program_of_study'], 
        gender = data['gender']
    )
    db.session.add(student_profile)
    db.session.commit()


def create_hostel_manager_profile(data):
    hostel_manager = HostelManager(
        user = data['user'],
        first_name = data['first_name'], 
        last_name=data['last_name'], 
        other_names=data['other_name'], 
        phone_number = data['phone_number'], 
        gender = data['gender']
    )
    db.session.add(hostel_manager)
    db.session.commit()

