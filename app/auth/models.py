from ..db import db, BaseModelMixin

class User(db.Model, BaseModelMixin):
    __tablename__ = 'ms_user'
    
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(250), unique=True)
    password = db.Column(db.String(250))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    active_status = db.Column(db.String(1))