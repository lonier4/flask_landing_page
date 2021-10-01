from flask_sqlalchemy import SQLAlchemy

#instantiate an instnace of our ORM to handle database communication
db = SQLAlchemy()    # you can name this variable anything you want

# define a model - a model is  going to be an entity/a table in our database
# and we can define it with the SQL CREATE TABLE in mind(what do I want? what SQL database tyoes will those columns be? COnstraints?)

class Animation(db.Model):  # lets our project know that Animation is a table in our database
    id = db.Column(db.Integer, primary_key=True)  # primary_key makes it a SERIAL
    name_of_show = db.Column(db.String(200), nullable=False, unique =True)
    network = db.Column(db.String(100))
    birthday_party_fee = db.Column(db.String(100))
    main_characters = db.Column(db.String(200))

    def to_dict(self):    # method to convert into a dictionary
        return {
            'id': self.id,
            'name_of_show': self.name_of_show,
            'network': self.network,
            'birthday_party_fee': self.birthday_party_fee,
            'main_characters': self.main_characters
        }