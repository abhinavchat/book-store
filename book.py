from book_store import app, db, login_manager
from book_store.models import Book, User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Book': Book, 'User': User}