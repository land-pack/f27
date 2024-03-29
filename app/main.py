from flask import Flask
from flask import render_template

app = Flask(__name__, static_url_path="")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")

if __name__ == '__main__':
    app.run(debug=True)
