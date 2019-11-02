from flask import Flask
from flask import render_template

app = Flask(__name__, static_url_path="")


@app.route("/home")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(port=5001)
