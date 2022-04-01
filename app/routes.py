from app import myobj
from flask import *
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


@myobj.route("/", methods=['GET', 'POST'])
def home():
    name = "Lisa"
    city_names=["Paris", "London" , "Rome" , "Tahiti"]
    error = None;
    if request.method == "POST":
            flash(request.form['pass'])
    return render_template("home.html",title="Home", name = name, city_names = city_names)
    

    
  
