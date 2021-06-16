from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,SubmitField,TextAreaField,RadioField
from wtforms.fields.core import FormField, SelectField
from wtforms.validators import DataRequired, Length, Required,Email
from wtforms import ValidationError



class SignupForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired("Please enter your First Name.")])
    last_name = StringField("Last Name", validators=[DataRequired("Please enter your Last Name")])
    email = StringField("Email", validators=[DataRequired("Please enter your email address."), Email("Pelase enter a valid email. name@host.com")])
    password = PasswordField("Password", validators=[DataRequired("Please enter your password"), Length(min=6,message="Passwords must be at least 6 characters in length.")])
    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired("Please enter your email address.")])
    password = PasswordField("Password", validators=[DataRequired("Please enter a password.")])
    submit = SubmitField("Sign In")

class PizzaForm(FlaskForm):
	title = StringField('Title', validators=[Required()])
	description = TextAreaField("Select a Pizza of your choice",validators=[Required()])
	category = RadioField('Label', choices=[ ('extra large ','extra large'), ('large pizza','large pizza'),('medium pizza','medium pizza'),('small pizza','small pizza')],validators=[Required()])
	submit = SubmitField('Submit:)')

class AddToCartForm(FlaskForm):
    pizza = StringField("What type of pizza would you like?", validators=[DataRequired("Please enter a pizza.")])
    # time = FormField(TimeForm)
    now_or_later = SelectField("Is your pizza for now or later?", choices=[("NOW", "Now"), ("LATER", "Later")])
    delivery = SelectField("Would you like your pizza delivered or take out?",choices=[("DELIVERY", "Delivery"), ("TAKEOUT", "Take Out")])
    submit = SubmitField("Place Order")