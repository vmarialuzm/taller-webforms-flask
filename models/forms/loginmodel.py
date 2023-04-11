from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,IntegerField,EmailField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username=StringField("Usuario",validators=[DataRequired()])
    name=StringField("Nombre",validators=[DataRequired()])
    last_name=StringField("Apellido",validators=[DataRequired()])
    age=IntegerField("Edad",validators=[DataRequired()])
    email=EmailField("Correo",validators=[DataRequired()])
    password=PasswordField("Contraseña",validators=[DataRequired()])
    remember_me=BooleanField("Recuerdame")
    submit=SubmitField("Enviar")