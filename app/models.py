from . import db

#...

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    
    def save_user(self):
        db.session.add(self)
        db.session.commit()
    def __repr__(self):
        return f'User {self.username}'
    
