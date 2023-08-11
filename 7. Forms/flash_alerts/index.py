from flask import Flask, render_template, flash, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config["SECRET_KEY"] = "jaykey"

class SimpleForm(FlaskForm):
    breed = StringField("What is the breed of your dog", validators=[DataRequired()])
    submit = SubmitField("Click me")
    
    
@app.route('/', methods=["GET", "POST"])
def index():
    form = SimpleForm()
    
    if form.validate_on_submit():
        session["breed"] = form.breed.data
        flash(f'Your breed is: {session["breed"]}')
        return redirect(url_for("index"))
    
    return render_template("index.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)