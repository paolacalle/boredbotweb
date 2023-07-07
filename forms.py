from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


#declare type 
#declare field label
#validate data 
class activityForm(FlaskForm):
  #DataRequired(field can not be left blank )
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)]) #min 2 and max 20 chars
    
    submit = SubmitField('Get Activity') #button that says Sign Up for submitting form 

class RegistrationForm(FlaskForm):
  #DataRequired(field can not be left blank )
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)]) #min 2 and max 20 chars
    
    email = StringField('Email',
                        validators=[DataRequired(), Email()]) #Email has a special vaildator 
    
    password = PasswordField('Password', validators=[DataRequired()])
    
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')]) #Checks they are equal 
    
    submit = SubmitField('Sign Up') #button that says Sign Up for submitting form 





