from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", title="Home")


@app.route("/use")
def use():
    return render_template("use.html", title="Use App")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=23333)