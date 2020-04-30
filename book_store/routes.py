from flask import flash, render_template, redirect, url_for, request
from book_store import app, db
from book_store.models import Book
from book_store.forms import AddBookForm, EditBookForm
import requests



@app.route('/')
@app.route('/home')
def home():
    books = Book.query.all()
    print(books)
    return render_template('index.html', title='Home', books = books)


@app.route('/book', methods=['GET', 'POST'])
def add_book():
    form = AddBookForm()
    if form.validate_on_submit():
        book = Book(title=form.title.data, 
        preview_url=form.preview_url.data, 
        description=form.description.data, 
        pages=form.pages.data,
        authors=form.authors.data)
        db.session.add(book)
        db.session.commit()
        flash(f"Book added successfully!")
        return redirect(url_for('home'))
    return render_template('book.html', form=form)


@app.route('/book/<id>', methods=['GET', 'POST'])
def book(id):
    book = Book.query.get_or_404(id)
    return render_template('book.html', book=book)


@app.route('/book/<id>/edit', methods=['GET', 'POST'])
def edit_book(id):
    book = Book.query.get_or_404(id)
    form = EditBookForm()
    if form.validate_on_submit():
        book.title = form.title.data
        book.description = form.description.data
        book.pages = form.pages.data
        book.preview_url = form.preview_url.data
        book.authors = form.authors.data
        
        db.session.add(book)
        db.session.commit()
        flash(f'Book has been updated')
        return redirect(url_for('home'))
        
    form.title.data = book.title
    form.description.data = book.description
    form.pages.data = book.pages
    form.preview_url.data = book.preview_url
    form.authors.data = book.authors
    return render_template('edit_book.html', form=form)


@app.route('/book/<id>/delete')
def delete_book(id):
    book = Book.query.get_or_404(id)
    if book:
        db.session.delete(book)
        db.session.commit()
        flash(f'Your book deleted successfully!')
    return redirect(url_for('home'))
