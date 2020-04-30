from book_store import app, db
from book_store.models import Book, User

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Book': Book, 'User': User}