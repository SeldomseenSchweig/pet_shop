
from tkinter import CASCADE
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def connect_db(app):
  db.app = app
  db.init_app(app)


class Pet(db.Model):
    __tablename__ = 'pets'
    

    id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement=True)
    name = db.Column(db.String(100),
                    nullable= False)
    species = db.Column(db.String(100),
                    nullable= False)
    photo_url= db.Column(db.String(100), nullable=True, default="https://cdn.pixabay.com/photo/2021/06/07/13/46/user-6318005__340.png")
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)