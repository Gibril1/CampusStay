from main import app
import re
import jwt
import datetime

def createJWT(username):
    return jwt.encode(
        {'user':username,
         'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=30)
         },
           app.config['SECRET_KEY']
           )

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    return False



def validate_phone_number(string):
    pattern = r'^\D*(\d\D*){10}$'
    if re.match(pattern, string):
        return True
    return False







