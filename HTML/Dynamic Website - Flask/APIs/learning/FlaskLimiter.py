
# https://flask-limiter.readthedocs.io/en/stable/#using-flask-pluggable-views

from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@app.route("/slow")
@limiter.limit("1 per day")
def slow():
    return ":("

@app.route("/medium")
@limiter.limit("1/second", override_defaults=False)
def medium():
    return ":|"

@app.route("/fast")
def fast():
    return ":)"

@app.route("/ping")
@limiter.exempt
def ping():
    return "PONG"

if __name__ == '__main__':
	app.run(debug = True)