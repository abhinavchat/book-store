from flask import render_template
from book_store import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title='Home')