#!/usr/bin/python3
"""Write a script that starts a Flask web application.
"""


from flask import Flask, render_template
"""Initialize app.
"""
app = Flask(__name__)
"""routes definition.
"""


@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    return f"C {text}".replace("_", " ")


@app.route("/python/")
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    return f"Python {text}".replace("_", " ")


@app.route('/number/<int:n>/')
def number(n=1):
    try:
        return render_template(f"{n} is a number", n=n)
    except Exception as e:
        return (str(e))


@app.route("/number_template/<int:n>/")
def number_template(n=1):
    try:
        return render_template("5-number.html", n=n)
    except Exception as e:
        return (str(e))


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n=1):
    try:
        return render_template("6-number_odd_or_even.html", n=n)
    except Exception as e:
        return (str(e))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
