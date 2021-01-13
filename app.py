from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'it is hard to hack!'


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")


if __name__ == "__main__":  # it will vaildate only when file will be executed directly
    app.run(debug=True)
