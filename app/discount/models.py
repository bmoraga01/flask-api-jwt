from ..db import db, BaseModelMixin
from sqlalchemy.dialects import sqlite, postgresql


class Discount(db.Model, BaseModelMixin):
    __tablename__ = 'ms_discount'
    
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    dt_id = db.Column(db.Integer(), db.ForeignKey('ms_discount_type.id'))
    desc = db.Column(db.String(150))
    nominal = db.Column(sqlite.NUMERIC(12))
    # msd_nominal = db.Column(postgresql.NUMERIC(12))
    active_status = db.Column(db.String(1))

class DiscountType(db.Model, BaseModelMixin):
    __tablename__ = 'ms_discount_type'
    
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    desc = db.Column(db.String(200))
    active_status = db.Column(db.String(1))
    # relation config with ms_discount
    discount_type = db.relationship('Discount', backref='discount_type')