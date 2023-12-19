import os

from flask import Flask, redirect, render_template, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from forms import AddForm, AddOwnerForm, DelForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"


############################
### SQL DATABASE SECTION ###
############################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "data.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app, db)


##############
### MODELS ###
##############


class Puppy(db.Model):
    __tablename__ = "puppies"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship("Owner", backref="Puppy", uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"{self.id}: Puppy name is {self.name} and Owner name is {self.owner.name}"
        else:
            return f"{self.id}: Puppy name is {self.name} and has no owner yet"


class Owner(db.Model):
    __tablename__ = "owners"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    puppy_id = db.Column(db.Integer, db.ForeignKey("puppies.id"))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f"Owner name: {self.name}"


###################################
### VIEW FUNCTIONS - HAVE FORMS ###
###################################


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_pup():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for("list_pup"))

    return render_template("add_puppy.html", form=form)


@app.route("/list")
def list_pup():
    puppies = Puppy.query.all()
    owners = Owner.query.all()
    return render_template("list_puppy.html", puppies=puppies, owners=owners)


@app.route("/delete", methods=["GET", "POST"])
def del_pup():
    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for("list_pup"))
    return render_template("delete_puppy.html", form=form)


@app.route("/add-owner", methods=["GET", "POST"])
def add_owner():
    form = AddOwnerForm()

    if form.validate_on_submit():
        id = form.id.data
        name = form.name.data
        owner = Owner(name, id)

        db.session.add(owner)
        db.session.commit()

        return redirect(url_for("list_pup"))
    return render_template("add_owner.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)

# export FLASK_APP=adoption_site.py (for MAC) / set FLASK_APP=models.py (for Windows)
# flask db init
# flask db migrate -m "initial migration"
# flask db upgrade
