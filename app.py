from flask import Flask, render_template
from config import Config
import os

app = Flask(__name__)


@app.route("/")
def index():
    navn = "Car Inventory"
    return render_template("index.html", navn=navn)
    


app.config.from_object(Config)

