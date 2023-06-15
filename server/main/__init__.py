from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_admin import Admin
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
load_dotenv()

import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Init app
app = Flask(__name__)
# Init cors
cors = CORS(app)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'instance/models.db')
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
# print(os.getenv('DATABASE_URL'))

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)
# Init admin
admin = Admin(app)
# Init bcrypt
bcrypt = Bcrypt(app)


from main.routes import user_routes
from .utils.admin import UserModelView
