from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from config import Config

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
Bootstrap(app)

app.config.from_object(Config)

from book_store import routes
