from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import User

from forms import *
app = Flask(__name__)
app.secret_key = 'it is hard to hack!'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jlbogoeijkdgra:f66d70134f07635fe3a7106c186ac24b6042b0beef003dec056247d512d21c2d@ec2-79-125-59-247.eu-west-1.compute.amazonaws.com:5432/d7ekrn4ndm767n'
#psql link_to_postgres_heroku
#CREATE TABLE users (
# id SERIAL PRIMARY KEY,
# username VARCHAR (25) UNIQUE NOT NULL
# password TEXT NOT NULL
# );
# \dt
# \d users

db = SQLAlchemy(app)


@app.route("/", methods=['GET', 'POST'])
def index():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        user_object = User.query.filter_by(username=username).first()
        if user_object:
            return "Someone else has taken this username!"

        user = User(username=username, password= password)
        db.session.add(user)
        db.session.commit()
        return "inserted into DB!"
    return render_template("index.html", form=reg_form)


if __name__ == "__main__":  # it will vaildate only when file will be executed directly
    app.run(debug=True)
