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

if __name__ == '__main__':
    app.run(debug = True)