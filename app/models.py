from . import db

#Create class for Users
class User(db.Model):
    '''
    Class to define users
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(255))
    pitches = db.relationship('User', backref = 'user', lazy = "dynamic")

    def __repr__(self):
        return f'User{self.username}'


class Pitch(db.Model):
    __tablename__ = 'pitches'
    
    id = db.Column(db.Integer,primary_key= True)
    category = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    def __repr__(self):
        return f"Pitch {self.category}"



