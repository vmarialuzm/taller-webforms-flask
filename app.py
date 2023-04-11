from flask import Flask,render_template,redirect,flash,url_for
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models.forms.loginmodel import LoginForm

app=Flask(__name__)
app.config.from_object(Config)

db=SQLAlchemy(app)
migrate=Migrate(app,db)

@app.route("/",methods=["GET","POST"])
def login():
    formulario=LoginForm()

    if formulario.validate_on_submit():
        flash("Inicio de sesión solicitado por {}, ¿Recuerdame? {}"
              .format(formulario.username.data,formulario.remember_me.data))
        return redirect(url_for('css'))
    return render_template("formulario.html",form=formulario)

@app.route("/css")
def css():
    return render_template("css.html")
