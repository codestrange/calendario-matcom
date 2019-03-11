from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView as _ModelView
from wtforms import PasswordField
from wtforms.validators import DataRequired

admin = Admin(name='Calendario MatCom', template_mode='bootstrap3')


class ModelView(_ModelView):
    can_delete = False
    can_view_details = True
    column_display_pk = True


class UserModelView(ModelView):
    column_exclude_list = form_excluded_columns = column_details_exclude_list = ['password_hash']
    form_extra_fields = {
        'password': PasswordField('Password', validators=[DataRequired()])
    }

    def on_model_change(self, form, model, is_created):
        model.password = form.password.data
