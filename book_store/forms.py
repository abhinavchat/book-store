from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Length, EqualTo, Email
from book_store.models import Book, User

def fetch_books():
        books =  Book.query.order_by(Book.title.desc()).all()
        return [(b.id, b.title) for b in books]


class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Length(min=0, max=500)])
    preview_url = StringField('Preview url')
    pages = IntegerField('Page Count', validators=[DataRequired()])
    authors = StringField('Author', validators=[DataRequired()], description="Comma-separated author names")
    


class AddBookForm(BookForm):
    submit = SubmitField('Add')
    
    def validate_title(self, title, extra_validators=None):
        t = Book.query.filter_by(title=title.data).first()
        if t:
            raise ValidationError('This title already exists!')


class EditBookForm(BookForm):
    submit = SubmitField('Edit')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired()])
    password2 = StringField('Confirm Password', validators=[DataRequired(), EqualTo('password', message=f'Password and Confirm Passwords must be same')])
    submit = SubmitField('Register')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(f"Username ({username.data}) already taken.")


    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(f"Email ({email.data}) already exists.")
