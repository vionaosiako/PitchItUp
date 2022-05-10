from flask import Flask, render_template,redirect,flash,url_for,request
from app import app,db,bcrypt
from app.models import User, Pitch,Comment
from .forms import *
from flask_login import current_user,logout_user,login_required
# login_user
@app.route('/')
@app.route('/index')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    pitches = Pitch.query.all()
    pitch_Sale = Pitch.query.filter_by(category_name = 'Sale pitch')
    # comment = Comment.filter_by(pitch_id='')
    return render_template('index.html',pitches=pitches, pitch_Sale=pitch_Sale)

@app.route('/pitchsale')
def pitchsalecategory():
    pitch_Sale = Pitch.query.filter_by(category_name = 'Sales')
    return render_template('pitchsale.html', pitch_Sale=pitch_Sale)

@app.route('/Elevatorpitch')
def pitchelevatorycategory():
    pitch_Elevator = Pitch.query.filter_by(category_name = 'Evevator')
    return render_template('Elevatorpitch.html', pitch_Elevator=pitch_Elevator)

@app.route('/Productpitch')
def pitchproductcategory():
    pitch_product = Pitch.query.filter_by(category_name = 'Product')
    return render_template('Productpitch.html', pitch_product=pitch_product)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        # hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created successfully. You can now login', 'success')
        return redirect(url_for('signIn'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error in creating the user:(err_msg)')
    return render_template('signup.html', form= form)

@app.route('/signIn', methods=['GET', 'POST'])
def signIn():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form=LogInForm()
    if form.validate_on_submit():
        # if form.validate_on_submit():
        #     user = User.query.filter(User.username == form.username.data).first()
        #     if user and bcrypt.check_password_hash(user.password, form.password.data):
        #         flash("you were just logged in!")
        #         login_user(user)
        #         return redirect(url_for("index"))
        #     else:
        #         flash("bad username or password")
        user = User.query.filter_by(username=form.username.data).first()
        return redirect(url_for('index'))
        if user and password(user.password, form.password.data):
            login_user(user,remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. PLease check email and password', 'danger')
    return render_template('login.html', title = 'Login', form= form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('signIn'))

@app.route('/comment', methods=['GET', 'POST'])
def comment():
    form=CommentForm()
    if form.validate_on_submit():
        comment = Comment(username= form.username.data, comment = form.comment.data)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been add successful')
        return redirect(url_for('index'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error when add the comment:(err_msg)')
    return render_template('comment.html', form= form)

@app.route('/addapitch', methods=['GET', 'POST'])
# @login_required
def addpitch():
    form=AddPitchForm()
    if form.validate_on_submit():
        pitch = Pitch(email=form.email.data, title=form.title.data, content=form.content.data, category_name = form.category_name.data)
        db.session.add(pitch)
        db.session.commit()
        flash('Your pitch has been add successful')
        return redirect(url_for('index'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error in creating the pitch:(err_msg)')
    
    return render_template('addPitch.html', form= form)

# @app.route('/dislike', methods=['GET', 'POST'])
# def dislike():

#     new_dislike = Downvote(user_id=current_user.id,pitch_id=id)
#     db.session.add(new_dislike)
#     db.session.commit()
#     return redirect(url_for('.index'))

