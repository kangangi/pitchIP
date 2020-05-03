from . import db

#Create class for Users
class User(db.Model):
    '''
    Class to define users
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User{self.username}'