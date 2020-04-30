from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from config import create_config
import os
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(create_config[os.getenv('ENVIRONMENT') or 'dev'])

db = SQLAlchemy(app)
migrate = Migrate(app, db)
Bootstrap(app)
login_manager = LoginManager(app)
login_manager.login_view = '/login'


from book_store import routes