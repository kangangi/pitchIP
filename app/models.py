from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
#Create class for Users
class User(UserMixin,db.Model):
    '''
    Class to define users
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(255))
    email = db.Column(db.String,unique = True)
    pitches = db.relationship("Pitch", backref = 'user', lazy = "dynamic")
    bio = db.Column(db.String(255))
    profile_pic_url = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    
    @property
    def password(self):
        raise AttributeError ('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User{self.username}'

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer,primary_key= True)
    category_name = db.Column(db.String())
    pitches = db.relationship("Pitch", backref ="category", lazy= "dynamic")

    @classmethod
    def get_category_name(cls,category_name):
        categoryName = Category.query.filter_by(category_name = category_name).first()
        return categoryName.id

    def __repr__(self):
        return f'Category{self.category_name}' 

    
class Pitch(db.Model):
    __tablename__ = 'pitches'
    
    id = db.Column(db.Integer,primary_key= True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    date = db.Column(db.DateTime,default=datetime.utcnow)
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship("Comment", backref ='pitch', lazy = "dynamic")
  
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_user_pitch(cls,id):
        user_pitches = Pitch.query.filter_by(user_id = id).all()
        return user_pitches

    @classmethod
    def get_category_pitch(cls,id):
        category_pitches = Pitch.query.filter_by(category_id = id).all()
        return category_pitches


    def __repr__(self):
        return f"Pitch {self.title}"

class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String())
    date =db.Column(db.DateTime,default = datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))


    def save_comment(self):
        db.sesssion.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(pitch_id = id).all()
        return comments



