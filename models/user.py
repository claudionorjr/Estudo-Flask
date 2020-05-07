from src.sql_alchemy import db
import datetime
from flask_restful import Resource, reqparse
from flask_login import UserMixin
from models.book import Book
from models.fk_books_in_users import books_in_users

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(84), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True, index=True)
    cpf = db.Column(db.String(84), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now())
    profile = db.Column(db.Boolean, default=False)
    books = db.relationship("Book",
        secondary=books_in_users,
        lazy=True,
        backref=db.backref('users')
    )

    def __str__(self):
        return self.name
