from flask_wtf import  FlaskForm
from wtforms import StringField,IntegerField,SubmitField


class AddOwnerForm(FlaskForm):
    
    name = StringField("Name of the Owner ::")
    puppy_id = IntegerField("Enter Puppy Id you want to adopt ::")
    submit = SubmitField("Add Owner")

class DeletePuppyForm(FlaskForm):

    puppy_id = IntegerField("Enter Puppy Id you adopted ::")
    submit = SubmitField("Remove Puppy")

class AddPuppyForm(FlaskForm):

    name = StringField("Name of the Puppy ::")
    submit = SubmitField("Add Puppy")



