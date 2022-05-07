from . import db

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(100),index = True)
    email = db.Column(db.String(100),unique = True,index = True)
    password = db.Column(db.String())
    pitchtable = db.relationship('Pitch', backref='user', lazy="dynamic")
    commenttable = db.relationship('Comment', backref='user', lazy="dynamic")
    def save_user(self):
        db.session.add(self)
        db.session.commit()
    def __repr__(self):
        return f'User {self.username}'
    
class Pitch(db.Model):
    __tablename__ = 'pitchtable'
    pitch_id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(100), index=True)
    content = db.Column(db.String(500), index=True)
    category_name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    commenttable = db.relationship('Comment', backref='pitch', lazy="dynamic")
    def save_pitch(self, pitch):
        ''' Save the pitches '''
        db.session.add(pitch)
        db.session.commit()
    def __repr__(self):
        return f"Pitch('{self.title}')"
    
class Comment(db.Model):
    __tablename__ = 'commenttable'
    comment_id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(500), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitchtable.pitch_id"))
    def save_comment(self, comment):
        ''' Save the comment '''
        db.session.add(pitch)
        db.session.commit()
    def __repr__(self):
        return f"Pitch('{self.comment}')"    
    