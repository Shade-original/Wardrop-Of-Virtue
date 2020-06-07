from flask import *
from flask_bootstrap import *

app = Flask(__name__)

@app.rooute("/")
def index():
    return render_templet("index.html")

