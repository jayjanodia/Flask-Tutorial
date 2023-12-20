import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = "mysecretkey"
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    base_dir, "data.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app, db)

# In order for db to be defined for the time when blueprints will use them, we need to define them after db has been defined

from project.owners.views import owners_blueprints
from project.puppies.views import puppies_blueprint

app.register_blueprint(owners_blueprints, url_prefix="/owners")
app.register_blueprint(puppies_blueprint, url_prefix="/puppies")
