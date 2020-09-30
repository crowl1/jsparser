from private_data import db_password
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import create_engine

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://postgres:{db_password}@localhost/first'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Films(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(256), nullable = True)
    year = db.Column(db.Integer)

    def __repl__(self):
        return f'id = {id}'

class Members(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(256), nullable = True)

    def __repl__(self):
        return f'id = {id}'

class Films_Members(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    id_film = db.Column(db.Integer, db.ForeignKey('films.id'))
    id_member = db.Column(db.Integer, db.ForeignKey('members.id'))

engine = create_engine(f'postgresql+psycopg2://postgres:{db_password}@localhost/first')

db.create_all()
db.session.commit()
engine.connect()