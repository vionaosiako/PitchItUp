from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')
    
class LogInForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')
    
class CommentForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    comment = StringField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')
    
class AddPitchForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    title =StringField('Title', validators=[DataRequired()])
    newPitch =StringField('Pitch Content', validators=[DataRequired()])
    category=StringField('Pitch Category', validators=[DataRequired()])
    submit = SubmitField('Add Pitch')
    