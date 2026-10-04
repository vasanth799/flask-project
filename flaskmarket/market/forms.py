from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,EqualTo,Email,ValidationError,DataRequired
from market.models import User

class RegisterForm(FlaskForm):

    def validate_username(self,username_to_check):
        user=User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('username already exists! please try a different username:')
    def validate_email_address(self,email_address_to_check):
            email=User.query.filter_by(email_address=email_address_to_check.data).first()
            if email:
                raise ValidationError('email already exists! please try a different email:')


        
    username=StringField(label='user_name',validators=[Length(min=2,max=30),DataRequired()])
    email_address=StringField(label='email',validators=[Email(),DataRequired()])
    password1=PasswordField(label='enter the password',validators=[Length(min=6),DataRequired()])
    password2=PasswordField(label='confirm password',validators=[EqualTo('password1'),DataRequired()])
    submit=SubmitField(label='submit')

class Loginform(FlaskForm):
     username=StringField(label='username',validators=[DataRequired()])
     password=PasswordField(label='password',validators=[DataRequired()])
     submit=SubmitField(label='sign in')

class purchaseitemform(FlaskForm):
    submit=SubmitField(label='purchase item!')

class sellitemform(FlaskForm):
    submit=SubmitField(label='sell item!')