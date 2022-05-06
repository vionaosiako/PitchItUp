from flask import Flask,render_template
# from flask_wtf import FlaskForm
# from wtform import StringField, PasswordField, BooleanField
# from wtforms.validator import InputRequired, Email, Length

app = Flask(__name__)



# class LoginForm()

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)