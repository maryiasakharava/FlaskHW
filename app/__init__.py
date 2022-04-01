from flask import *
from wtforms import *
from wtforms.validators import DataRequired

myobj = Flask(__name__)
myobj.secret_key = "abc"



from app import routes
