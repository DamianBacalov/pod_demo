from flask import Flask
import os
import os.path


app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app.config.from_object('config')

from application import views


