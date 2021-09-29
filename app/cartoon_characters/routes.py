# within your blueprint's routes file - the first step is to instantaite 
# the blueprint and make sure that the blueprint is registered and can communicate with the larger app

from flask import Blueprint, render_template

# create the instance o four blueprint
character = Blueprint('cartoon_characters', __name__, template_folder='cartoon_characters_templates')

#when we're using blueprints - our routing decorator syntax is slightly changed
# @<blueprint_name>.route('/<url_endpoint>', [methods=<'GET','POST','PUT'>])
# def <routefuncname>():

# from here its like our other routes.py file - just creating routes for our movies blueprint
@character.route('/favoritecartoon')
def favoritecartoon():
    cartoon_of_the_day = 'Tom & Jerry'
    return render_template('favoritecartoon.html', cartoon = cartoon_of_the_day)