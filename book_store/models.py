from book_store import app, db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, index=True)
    email = db.Column(db.String(50), unique=True, index=True)
    phone = db.Column(db.String(10), unique=True, index=True)
    password_hash = db.Column(db.String(120))