from ..db import db, BaseModelMixin
from sqlalchemy.dialects import sqlite, postgresql


class Discount(db.Model, BaseModelMixin):
    __tablename__ = 'ms_discount'
    
    msd_id = db.Column(db.Integer(), primary_key=True)
    msd_msdt_id = db.Column(db.Integer(), db.ForeignKey('ms_discount_type.msdt_id'))
    msd_desc = db.Column(db.String(150))
    msd_nominal = db.Column(sqlite.NUMERIC(12))
    # msd_nominal = db.Column(postgresql.NUMERIC(12))
    msd_active_status = db.Column(db.String(1))

class DiscountType(db.Model, BaseModelMixin):
    __tablename__ = 'ms_discount_type'
    
    msdt_id = db.Column(db.Integer(), primary_key=True)
    msdt_desc = db.Column(db.String(200))
    msdt_active_status = db.Column(db.String(1))
    # relation config with ms_discount
    discount_type = db.relationship('Discount', backref='discount_type')