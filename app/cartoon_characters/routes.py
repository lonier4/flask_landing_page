# within your blueprint's routes file - the first step is to instantaite 
# the blueprint and make sure that the blueprint is registered and can communicate with the larger app

from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.forms import newCartoonForm

# database imports
from app.models import db, Animation

# create the instance o four blueprint
character = Blueprint('cartoon_characters', __name__, template_folder='cartoon_characters_templates')

#when we're using blueprints - our routing decorator syntax is slightly changed
# @<blueprint_name>.route('/<url_endpoint>', [methods=<'GET','POST','PUT'>])
# def <routefuncname>():

# from here its like our other routes.py file - just creating routes for our movies blueprint
@character.route('/favoritecartoon')
def favoritecartoon():
    list_of_characters = "Bender from Futurama", "Arthur", "Bart Simpson", "Finn & Jake from Adventure Time" 
    return render_template('favoritecartoon.html', a_cartoon = list_of_characters)

@character.route('/addcartoon', methods=['GET', 'POST'])
def addcartoon():
    form = newCartoonForm()
    if request.method == 'POST':
        # do stuff with the form that the user submitted
        # first we need to check if the form validates
        if form.validate_on_submit():
            # create an instance of our Animation table
            # keywords should match what is in your models.py
            new_cartoon = Animation(name_of_show=form.name_of_show.data, network=form.network.data, birthday_party_fee=form.birthday_party_fee.data, main_characters=form.main_characters.data)
            
            # put that instance of Animation into our database
            db.session.add(new_cartoon)
            db.session.commit()
            
            # you can use the 'new_cartoon' instance and pass the .to_dict method to display what was added
            flash('New Cartoon Added!', category='alert-info')
            flash(f'{new_cartoon.to_dict()}', category='alert-info')
        else:
            flash('Nop, try again buddy', category='alert-danger')

        return redirect(url_for('cartoon_characters.addcartoon'))
        # implied else when request.method == 'GET'
        # We just render the html file like normal
    return render_template('addcartoon.html', form=form)