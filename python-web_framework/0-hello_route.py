#!/usr/bin/python3
"""Write a script that starts a Flask web application.
"""


from flask import Flask
"""Initialize app.
"""
app = Flask(__name__)
"""routes definition.
"""

@app.route("/",strict_slashes = False)
def home():
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port="5000")