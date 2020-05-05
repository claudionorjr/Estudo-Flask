from data.sql_alchemy import db
import datetime
from flask_restful import Resource, reqparse
from flask_login import UserMixin

class Book(db.Model, UserMixin):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(125), nullable=False)

    def __str__(self):
        return self.name
