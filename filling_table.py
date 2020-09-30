from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import create_engine

from private_data import db_password
from create_table import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://postgres:{db_password}@localhost/first'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

def filling(data_film):

    for data in data_film:

        film = Films(title = data['title'], year = data['year'])
        db.session.add(film)

        db.session.flush()

        for item in data['members']:

            member_list = Members.query.filter_by(name = item).all()
            
            if len(member_list) == 0:
                member = Members(name = item)
                db.session.add(member)
                db.session.flush()


            db.session.add(Films_Members(id_film = film.id, id_member = member.id or member_list[0].id))

        db.session.commit()
