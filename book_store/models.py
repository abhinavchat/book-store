from book_store import app, db
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, index=True)
    preview_url = db.Column(db.String(200))
    description = db.Column(db.String(500))
    pages = db.Column(db.Integer)
    authors = db.Column(db.String)

    def __repr__(self):
        return f"<Book {self.title}>"
