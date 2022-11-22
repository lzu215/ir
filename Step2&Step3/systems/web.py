# Imports

from flask import Flask, request, render_template, url_for
from time import sleep
from sys import path
from pathlib import Path
from core import configs


# Constants

ROOT = Path.cwd()
TEMPLATES = ROOT/"templates"


# Miscellaneous

path.append(str(ROOT.parents[0]))
app = Flask(__name__,  template_folder = str(TEMPLATES))


# Routing

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/<string:function>", methods = ("POST",))
def api():
    pass


# Main

def main():
    app.run()


if __name__ == "__main__":
    main()