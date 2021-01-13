from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length


class RegistrationForm(FlaskForm):
    """ Registration form"""

    username = StringField('username',
                           validators=[InputRequired(message="Username required"),
                                       Length(min=4, max=20, message="should be between 4 and 20")])
    password = PasswordField('password',
                             validators=[InputRequired(message="Username required"),
                                         Length(min=4, max=20, message="should be between 4 and 20")])
    confirm_password = PasswordField('confirm_password',
                                     validators=[InputRequired(message="Username required"),
                                                 Length(min=4, max=20, message="should be between 4 and 20")])
    submit_button = SubmitField('Create')