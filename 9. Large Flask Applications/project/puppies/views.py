from flask import Blueprint, redirect, render_template, url_for
from project import db
from project.models import Puppy
from project.puppies.forms import AddForm, DelForm

puppies_blueprint = Blueprint("puppies", __name__, template_folder="templates/puppies")


@puppies_blueprint.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for("puppies.list"))

    return render_template("add_puppies.html", form=form)


@puppies_blueprint.route("/list")
def list():
    puppies = Puppy.query.all()
    return render_template("list_puppies.html", puppies=puppies)


@puppies_blueprint.route("/delete", methods=["GET", "POST"])
def delete():
    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for("puppies.list"))
    return render_template("delete_puppies.html", form=form)
