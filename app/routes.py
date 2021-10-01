from flask.templating import render_template
from app import app

@app.route('/')
def home():
    cartoon_of_the_day = 'Tom & Jerry'
    return render_template('index.html', cartoon = cartoon_of_the_day)
