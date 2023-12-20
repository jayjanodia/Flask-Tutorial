from flask import render_template
from project import app


@app.route("/")
def index():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)

# RUN MIGRATIONS USING
# export FLASK_APP=index.py (for Mac) / set FLASK_APP=index.py (for Windows)
# flask db init (will generate migrations folder)
# flask db migrate -m "Created Puppy table"
# flask db upgrade
