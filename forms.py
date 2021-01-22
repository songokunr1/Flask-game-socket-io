from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import InputRequired, Length, ValidationError

from models import *


def invalid_credentials(form, field):
    """Username and password checker"""
    """ form and field will be automaticly passed to the validator"""
    username_entered = form.username.data
    password_entered = field.data
    user_object = User.query.filter_by(username=username_entered).first()
    if user_object is None:
        raise ValidationError("username is not correct :( ")
    if user_object.password != password_entered:
        raise ValidationError("password is not correct")


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

    def validate_username(self, username):
        """ naming:
        validate_parametrname -> in our case username,
        args: name of parametr """

        user_name = User.query.filter_by(username=username.data).first()
        if user_name:
            raise ValidationError("Username already exist")


class LoginForm(FlaskForm):
    """ login Form"""

    username = StringField('username',
                           validators=[InputRequired(message="Username required")])
    password = PasswordField('password',
                             validators=[InputRequired(message="Password required"), invalid_credentials])
    submit_button = SubmitField('Login')


class WybierzKarte(FlaskForm):
    """wybor karty """

    karta = StringField("Karta", validators=[])
    potwierdz = SubmitField("potweirdz wybor", validators=[])


class ChooseCard(FlaskForm):
    def __init__(self, cards, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cards.choices = [(card, card) for card in
                        cards]

    cards = SelectField('Select Card')
    submit = SubmitField()
