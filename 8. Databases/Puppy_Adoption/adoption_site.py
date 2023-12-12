import os

from flask import Flask, redirect, render_template, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from forms import AddForm, DelForm

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

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Puppy name: {self.name}"


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
    return render_template("list_puppy.html", puppies=puppies)


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


if __name__ == "__main__":
    app.run(debug=True)

# export FLASK_APP=adoption_site.py (for MAC) / set FLASK_APP=models.py (for Windows)
# flask db init
# flask db migrate -m "initial migration"
# flask db upgrade
