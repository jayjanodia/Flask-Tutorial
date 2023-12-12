import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#Put the SQLite database in this directory. You will get the absolute path to the directory this file is present in
# 8. Databases
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.app_context().push()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, 'data.sqlite')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# RUN MIGRATIONS USING
# export FLASK_APP=index.py (for Mac) / set FLASK_APP=index.py (for Windows)
# flask db init (will generate migrations folder)
# flask db migrate -m "Created Puppy table"
# flask db upgrade

Migrate(app, db)

class Puppy(db.Model):
    # MANUAL TABLE NAME CHOICE
    __tablename__ = 'puppies'
    
    # Create columns
    id = db.Column(db.Integer, primary_key = True) #auto created
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)
    
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        
    def __repr__(self):
        '''Gives the string representation of the object'''
        return f"Puppy {self.name} is {self.age} years old"