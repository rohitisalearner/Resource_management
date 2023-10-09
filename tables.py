from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, ForeignKey
db = SQLAlchemy()

class UserLogin(db.Model):    
    __tablename__ = 'UserLogin'
    id= db.Column(db.Integer, primary_key=True)
    userName=db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), unique=False)
    token= db.Column(db.String(200), unique=True)
    expireTime=db.Column(db.String(100), unique=False)

class Assets(db.Model):    
    __tablename__ = 'Assets'
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(100))
    serialNo = db.Column(db.String(100), unique=True)
    Date=db.Column(db.DateTime)
    cost=db.Column(db.String(100))
    userId=db.Column(db.String(100))
    model=db.Column(db.String(100))

class Category(db.Model):    
    __tablename__ = 'Category'
    id= db.Column(db.Integer, primary_key=True)
    AssetsId=db.Column(db.String(100), unique=True)
    categoryName = db.Column(db.String(100), unique=True)

class Images(db.Model):    
    __tablename__ = 'Images'
    id= db.Column(db.Integer, primary_key=True)
    AssetsImageId=db.Column(db.String(100), unique=True)
    categoryImageName = db.Column(db.String(100), unique=True)

class Assigned(db.Model):
    __tablename__ = 'Assigned'
    id= db.Column(db.Integer, primary_key=True)
    UsersId =Column(Integer, ForeignKey('Users.id'))
    assetId = Column(Integer, ForeignKey('Assets.id'),unique=True)
    Date = db.Column(db.DateTime)
    pageSeos=db.relationship("Users", backref='Assigned')

class Users(db.Model):
    __tablename__ = 'Users'
    id= db.Column(db.Integer, primary_key=True)
    userName=db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=False)
    dob= db.Column(db.String(100))