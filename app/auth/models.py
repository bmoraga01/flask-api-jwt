import datetime
from ..db import db, BaseModelMixin
from flask_bcrypt import  generate_password_hash, check_password_hash

class User(db.Model, BaseModelMixin):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(250), unique=True)
    password = db.Column(db.String(250))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    active_status = db.Column(db.String(1))
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=True)
    
    def __init__(self, **kwargs):
        """
        The function takes in a dictionary of keyword arguments and assigns the values to the class
        attributes
        """
        self.username = kwargs.get("username")
        self.email = kwargs.get("email")
        self.password = kwargs.get("password")
        
    def __repr__(self):
        """
        The __repr__ function is used to return a string representation of the object
        :return: The username of the user.
        """
        return "<User {}>".format(self.username)
    
    def hash_password(self):
        """
        It takes the password that the user has entered, hashes it, and then stores the hashed password in
        the database
        """
        self.password = generate_password_hash(self.password).decode("utf8")
        
    def check_password(self, password):
        """
        It takes a plaintext password, hashes it, and compares it to the hashed password in the database
        
        :param password: The password to be hashed
        :return: The password is being returned.
        """
        return check_password_hash(self.password, password)