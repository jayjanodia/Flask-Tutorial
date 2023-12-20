from flask import Blueprint, redirect, render_template, url_for
from project import db
from project.models import Owner
from project.owners.forms import AddForm

owners_blueprints = Blueprint("owners", __name__, template_folder="templates/owners")


@owners_blueprints.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()

    if form.validate_on_submit():
        id = form.id.data
        name = form.name.data
        owner = Owner(name, id)

        db.session.add(owner)
        db.session.commit()

        return redirect(url_for("puppies.list"))
    return render_template("add_owner.html", form=form)
