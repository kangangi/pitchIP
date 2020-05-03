from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin


#Create class for Users
class User(UserMixin,db.Model):
    '''
    Class to define users
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(255))
    email = db.Column(db.String,unique = True)
    pitches = db.relationship('User', backref = 'user', lazy = "dynamic")
    pass_secure = db.Column(db.String(255))
    
    @property
    def password(self):
        raise AttributeError ('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User{self.username}'


class Pitch(db.Model):
    __tablename__ = 'pitches'
    
    id = db.Column(db.Integer,primary_key= True)
    category = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    def __repr__(self):
        return f"Pitch {self.category}"



