from app import db,login_manager,bcrypt
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model, UserMixin):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(100),unique = True,index = True)
    email = db.Column(db.String(100),unique = True,index = True)
    password = db.Column(db.String(255))
    pitchtable = db.relationship('Pitch', backref='user')
    commenttable = db.relationship('Comment', backref='user')
    def save_user(self, user):
        ''' Save the pitches '''
        db.session.add(user)
        db.session.commit()
    def __repr__(self):
        return f"Pitch('{self.username}')"
    

    
    # @property
    # def prettier_budget(self):
    #     if len(str(self.budget)) >= 4:
    #         return f'{str(self.budget)[:-3]},{str(self.budget)[-3:]}$'
    #     else:
    #         return f"{self.budget}$"

    # @property
    # def password(self):
    #     return self.password

    # @password.setter
    # def password(self, plain_text_password):
    #     self.password = bcrypt.generate_password(plain_text_password).decode('utf-8')

    # def check_password_correction(self, attempted_password):
    #     return bcrypt.check_password(self.password, attempted_password)
    # def password(self, password):
    #     """Set password."""
    #     self.password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    # @property
    # def password(self):
    #     return self.password

    # @password.setter
    # def password(self, value):
    #     bvalue = bytes(value, 'utf-8')
    #     temp_hash = bcrypt.hashpw(bvalue, bcrypt.gensalt())
    #     self.password = temp_hash.decode('utf-8')

    # def check_password(self, value):
    #     return bcrypt.checkpw(value.encode('utf-8'), self.password.encode('utf-8'))
    
    
    #return password
    # @property
    # def password(self):
    #     return self.password

    # @password.setter
    # def password(self, plain_text_password):
    #     self.password = bcrypt.generate_password(plain_text_password).decode('utf-8')

    # def check_password_correction(self, attempted_password):
    #     return bcrypt.check_password(self.password, attempted_password)
    
    
    
    # @property
    # def password(self):
    #     raise AttributeError('You cannot read the password attribute')
    # @password.setter
    # def password(self, password):
    #     self.pass_secure = generate_password_hash(password)
    # def verify_password(self,password):
    #     return check_password_hash(self.pass_secure,password)
    
class Pitch(db.Model):
    __tablename__ = 'pitchtable'
    pitch_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100),index = True)
    title = db.Column(db.String(100), index=True)
    content = db.Column(db.String(500), index=True)
    category_name = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    commenttable = db.relationship('Comment', backref='pitch')
    def save_pitch(self, pitch):
        ''' Save the pitches '''
        db.session.add(pitch)
        db.session.commit()
    def __repr__(self):
        return f"Pitch('{self.title}')"
    
class Comment(db.Model):
    __tablename__ = 'commenttable'
    comment_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100),index = True)
    comment = db.Column(db.String(500), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitchtable.pitch_id"))
    def save_comment(self, comment):
        ''' Save the comment '''
        db.session.add(pitch)
        db.session.commit()
    def __repr__(self):
        return f"Pitch('{self.comment}')"    
    