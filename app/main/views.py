from flask import Flask, render_template
from . import main
from .forms import *

@main.route('/')
@main.route('/index')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    form=RegistrationForm()
    return render_template('signup.html', form= form)

@main.route('/signIn', methods=['GET', 'POST'])
def signIn():
    form=LogInForm()
    return render_template('login.html', form= form)

@main.route('/comment', methods=['GET', 'POST'])
def comment():
    form=CommentForm()
    return render_template('comment.html', form= form)

@main.route('/addpitch', methods=['GET', 'POST'])
def addpitch():
    form=AddPitchForm()
    return render_template('addPitch.html', form= form)