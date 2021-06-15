from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError



class PizzaForm(FlaskForm):
	title = StringField('Title', validators=[Required()])
	description = TextAreaField("Rafiki, Select a Pizza of your choice",validators=[Required()])
	category = RadioField('Label', choices=[ ('extra large ','extra large'), ('large pizza','large pizza'),('medium pizza','medium pizza'),('small pizza','small pizza')],validators=[Required()])
	submit = SubmitField('Submit:)')