from main import admin, db
from flask_admin.contrib.sqla import ModelView

from ..models.user_models import User

class UserModelView(ModelView):
    column_display_pk = True
    column_list = ('username',)


admin.add_view(UserModelView(User, db.session))
