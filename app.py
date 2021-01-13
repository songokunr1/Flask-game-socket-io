from flask import Flask, render_template

from forms import *
app = Flask(__name__)
app.secret_key = 'it is hard to hack!'



@app.route("/", methods=['GET', 'POST'])
def index():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        return "Great!"
    return render_template("index.html", form=reg_form)


if __name__ == "__main__":  # it will vaildate only when file will be executed directly
    app.run(debug=True)
