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


def create_table():
    db.create_all()
    db.session.commit()
    engine.connect()
    print('tables created successfully')


if __name__ == "__main__":
    create_table()


def filling_table(data_film):

    for data in data_film:

        film = Films(title = data['title'], year = data['year'])
        db.session.add(film)

        db.session.flush()

        for item in data['members']:

            member_list = Members.query.filter_by(name = item.strip()).all()
            
            if len(member_list) == 0:
                member = Members(name = item.strip())
                db.session.add(member)
                db.session.flush()
                member_id = member.id
            else:
                member_id = member_list[0].id
                if (member_list[0].name == 'Robert De Niro'):
                    print('V')

            db.session.add(Films_Members(id_film = film.id, id_member = member_id ))

        db.session.commit()

    print('tables are successfully filled')