from flask import flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/methods", methods=["GET"])
def using_methods():
    return redirect()


if __name__ == "__main__":
    app.run(debug=True)