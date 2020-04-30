from book_store import db
import uuid
from werkzeug.security import check_password_hash, generate_password_hash

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, index=True)
    preview_url = db.Column(db.String(200))
    description = db.Column(db.String(500))
    pages = db.Column(db.Integer)
    authors = db.Column(db.String)

    def __repr__(self):
        return f"<Book {self.title}>"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(50), nullable=False)

    def __init__(self, username, email):
        self.public_id = str(uuid.uuid4())
        self.username = username
        self.email = email

    @property
    def password(self):
        raise AttributeError("Cannot get password propery. No such field exists.")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    @staticmethod
    def check_password(password):
        return self.password_hash == check_password_hash(password)


