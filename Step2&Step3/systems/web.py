# Imports

from flask import Flask, request, render_template
from sys import path
from pathlib import Path
from json import dumps
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


@app.route("/search/<string:system>", methods = ("POST",))
def search(system):
    if system in configs.modules:
        receive = customDict(request.values)
        result = configs.modules[system].execute(receive)
        result["page_size"] = configs[system].page_size
        return dumps(result)


@app.route("/system/<string:operation>", methods = ("POST",))
def system(operation):
    receive = customDict(request.values)
    result = getattr(configs.modules.system, operation)(receive)
    return dumps(result)


# Main

def main():
    app.run("0.0.0.0", 5000, True)


if __name__ == "__main__":
    main()