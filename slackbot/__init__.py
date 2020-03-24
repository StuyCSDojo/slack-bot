from flask import Flask, render_template
import os

app = Flask(__name__)
DIR = os.path.dirname(__file__) + "/"

@app.route("/")
def root():
    return render_template("index.html");

if __name__ == "__main__":
    app.run()
