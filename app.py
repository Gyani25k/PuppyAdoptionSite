import os
from flask import Flask,redirect,render_template,url_for,request
from flask_cors import CORS
from forms import AddOwnerForm,DeletePuppyForm,AddPuppyForm
from flask_sqlalchemy import SQLAlchemy
from db import db
from models import Puppies,Owner


app = Flask(__name__,template_folder='template')

CORS(app)

db=SQLAlchemy(app)


app.config['SECRET_KEY'] = "AdoptionSite@2023"


basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/addpuppiesV1',methods=['POST','GET'])
def add_puupies():
    form = AddPuppyForm()
    if form.validate_on_submit():

        name = form.name.data  

        puppy = Puppies(name=name)

        db.session.add(puppy)

        db.session.commit()

        return redirect(url_for('list_puppies'))

    return render_template('addpupies.html',form=form)

@app.route('/deletepuppiesV1', methods=['POST', 'GET'])
def delete_puppies():
    form = DeletePuppyForm()

    if form.validate_on_submit():
        id = form.puppy_id.data
        puppy = Puppies.query.get(id) 

        if puppy:
            db.session.delete(puppy)
            db.session.commit()

            return redirect(url_for('list_puppies'))

    return render_template('deletepuppies.html', form=form)

@app.route('/addownersV1',methods=['POST','GET'])
def add_owners():
    form = AddOwnerForm()

    if form.validate_on_submit():
        name = form.name.data
        puppyid = form.puppy_id.data

        owner  = Owner(name = name,puppy_id=puppyid)

        db.session.add(owner)
        db.session.commit()

        return redirect(url_for('list_puppies'))

    return render_template('addowner.html',form=form)

@app.route('/listallpuppiesV1')
def list_puppies():

    puppies = Puppies.query.all()

    return render_template('listpuppies.html', puppies=puppies)







if __name__ == "__main__":
    app.run(debug=True,port=8000)

