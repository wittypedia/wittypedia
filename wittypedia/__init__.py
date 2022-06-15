from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
import logging
from logging.handlers import RotatingFileHandler
import random
import os

random_string = ""
alnums = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

for i in range(32):
    random_string += alnums[random.randint(0, len(alnums) - 1)]

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = random_string
app.config['SESSION_COOKIE_SECURE'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
# run flask db migrate to make database changes
# run flask db upgrade to apply database changes
# flask db downgrade undoes the last migration
csrf = CSRFProtect()
csrf.init_app(app)

app.config['WTF_CSRF_SECRET_KEY'] = os.urandom(32)

from wittypedia import routes, models, errors

if not app.debug:

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log',
                                       maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(
        logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')