from main import ma 

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email_address', 'role')

user_schema = UserSchema()
users_schema = UserSchema(many = True)


class StudentProfileSchema(ma.Schema):
    class Meta:
        fields=('reference_number', 'user', 'first_name', 'last_name', 'other_names', 'phone_number', 'program_of_study', 'gender')

studentprofile_schema = StudentProfileSchema()
studentprofiles_schema = StudentProfileSchema(many=True)

class HostelManagerSchema(ma.Schema):
    class Meta:
        fields=('manager_id', 'user', 'first_name', 'last_name', 'other_names', 'phone_number', 'program_of_study', 'gender')

hostelmanager_schema = HostelManagerSchema()
hostelmanagers_schema = HostelManagerSchema(many=True)

