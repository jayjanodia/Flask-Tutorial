import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.app_context().push()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "data.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app, db)


class Puppy(db.Model):
    __tablename__ = "puppies"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    # ONE-TO-MANY relationship. We are connecting one puppy to many toys
    # First parameter: Connects to other model/database
    # Second parameter: Add a back reference to the other model in the relationship
    # Third parameter: Specifies how the items are to be loaded.
    toys = db.relationship("Toy", backref="Puppy", lazy="dynamic")

    # ONE-TO-ONE: One Puppy == One Owner
    # uselist should be set to false since we are having one-to-one relationship
    # Usually in one-to-many, one puppy would have a list of many toys, here we just have 1 owner so no list
    owner = db.relationship("Owner", backref="Puppy", uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Puppy name is {self.name} and Owner name is {self.owner.name}"
        else:
            return f"Puppy name is {self.name} and has no owner yet"

    def report_toys(self):
        print("Here are my toys:")
        for toy in self.toys:
            print(toy.item_name)


class Toy(db.Model):
    __tablename__ = "toys"

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey("puppies.id"))

    def __init__(self, item_name, puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id


class Owner(db.Model):
    __tablename__ = "owners"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    puppy_id = db.Column(db.Integer, db.ForeignKey("puppies.id"))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id


# export FLASK_APP=models.py (for MAC) / set FLASK_APP=models.py (for Windows)
# flask db init
# flask db migrate -m "initial migration"
# flask db upgrade
