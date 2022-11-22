# Imports

from flask import Flask, request, render_template
from sys import path
from pathlib import Path
from core import configs, customDict


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
def api(function):
    if function in configs.modules:
        receive = customDict(request.values)
        return str(configs.modules[function].execute(receive))


# Main

def main():
    app.run()


if __name__ == "__main__":
    main()