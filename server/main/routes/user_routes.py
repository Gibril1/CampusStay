from flask_cors import cross_origin
from main import app
from ..controllers.user_controllers import (
    register_user, 
    login_user
)


@app.route('/register', methods=['POST'])
@cross_origin()
def register():
    return register_user()


@app.route('/login', methods=['POST'])
@cross_origin()
def login():
    return login_user()



