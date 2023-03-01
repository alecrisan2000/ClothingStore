from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    first_name = db.Column(db.String(50))


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(50))
    name = db.Column(db.String(50), unique=True)
    price = db.Column(db.Double)
    stock = db.Column(db.Integer)


class Clothes(db.Model, Product):
    __tablename__ = 'clothes'
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String(2))
    color = db.Column(db.String(50))
    type = db.Column(db.String(6))
    __mapper_args__ = {
        'polymorphic_identity': 'clothes',
    }


class Shoe(db.Model, Product):
    __tablename__ = 'shoes'
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.Integer)
    __mapper_args__ = {
        'polymorphic_identity': 'shoes',
    }
