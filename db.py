import private_data
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

app.config['TestDB'] = f'postgresql://postgres:{db_password}@localhost/first'