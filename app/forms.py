# imports that I'll need to work with WTForms: generic form template, whatever types of data fields you intned to use, and whatever validators you intend to use.
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, IntegerField, DecimalField, SubmitField
from wtforms.validators import DataRequired

# creating a new form - we're going to be making a class that inherits some behavior from FlaskForm

class newCartoonForm(FlaskForm):
    # what we have inside this class is whatever data fields we intend our form to have
    name_of_show = StringField('Name', validators=[DataRequired()])
    network = StringField('Network')
    birthday_party_fee = StringField('Birthday Party Fee')  # if using DecimalField it could throw error if DataRequired is not applied and left empty
    main_characters = StringField('Main Characters')        # empty field is actually an empty string ''. Could also use StringField instead
    submit_button = SubmitField()