from book_store import app, db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, index=True)
    email = db.Column(db.String(50), unique=True, index=True)
    phone = db.Column(db.String(10), unique=True, index=True)
    password_hash = db.Column(db.String(120))

    def __repr__(self):
        return f"<User {self.username}>"

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    preview_url = db.Column(db.String(200))
    description = db.Column(db.String(500))
    pages = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

    def __repr__(self):
        return f"<Book {self.title}>"


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    books = db.relationship('Book', backref='author', lazy='dynamic')

    def __repr__(self):
        return f"<Author {self.name}>"
