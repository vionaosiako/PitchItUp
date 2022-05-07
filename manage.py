from flask import Flask,render_template

app = Flask(__name__)



# class LoginForm()

@app.route('/')
@app.route('/index')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form=RegistrationForm()
    return render_template('signup.html', form= form)

@app.route('/signIn', methods=['GET', 'POST'])
def signIn():
    form=LogInForm()
    return render_template('login.html', form= form)

@app.route('/comment', methods=['GET', 'POST'])
def comment():
    form=CommentForm()
    return render_template('comment.html', form= form)

@app.route('/addpitch', methods=['GET', 'POST'])
def addpitch():
    form=AddPitchForm()
    return render_template('addPitch.html', form= form)

if __name__ == '__main__':
    app.run(debug = True)