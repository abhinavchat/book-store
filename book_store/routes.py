from flask import render_template
from book_store import app
from book_store.models import User

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title='Home')

@app.route('/login')
def login():
    pass

@app.route('/logout')
def logout():
    pass


@app.route('/register')
def register():
    pass