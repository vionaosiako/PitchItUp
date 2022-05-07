from app import create_app
from flask_script import Manager,Server
# Creating app instance
app = create_app('development')
manager = Manager(app)
manager.add_command('server',Server)
if __name__ == '__main__':
    manager.run()

# from flask import Flask,render_template
# from forms import *

# app = Flask(__name__)

# if __name__ == '__main__':
#     app.run(debug = True)