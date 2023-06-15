
from main import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), nullable = False, unique = True)
    email_address = db.Column(db.String(100), nullable = False, unique = True)
    password = db.Column(db.String(100), nullable = False)
    role = db.Column(db.String(20), nullable = False, default='student')

    student = db.relationship('StudentProfile', backref='studentprofile', lazy = True)
    manager = db.relationship('HostelManager', backref='studentprofile', lazy = True)

    def __repr__(self):
        return f'User {self.username} - {self.email_address}'


class StudentProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reference_number = db.Column(db.String(20), unique=True, nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    first_name = db.Column(db.String(20), nullable = False)
    last_name = db.Column(db.String(20), nullable = False)
    other_names = db.Column(db.String(20))
    phone_number = db.Column(db.String(20), nullable = False)
    program_of_study = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=False)

    def __repr__(self) -> str:
        return f'Student f{self.reference_number} - {self.program_of_study}'


class HostelManager(db.Model):
    __tablename__ = 'hostelmanager'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20), nullable = False)
    last_name = db.Column(db.String(20), nullable = False)
    other_names = db.Column(db.String(20))
    phone_number = db.Column(db.String(20), nullable = False)
    gender = db.Column(db.String(10), nullable=False)

    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    hostel_manager = db.relationship('Hostel', backref = 'manager', lazy = True)

    def __repr__(self):
        return f'Manager {self.manager_id} - {self.user}'
    






