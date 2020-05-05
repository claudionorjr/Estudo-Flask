from data.sql_alchemy import db

books_in_users = db.Table("books_users",
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), nullable=False),
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), nullable=False)
)