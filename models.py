from db import db

class Puppies(db.Model):

    __tablename__ = "Puppies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    owners = db.relationship('Owner', back_populates='puppy')

class Owner(db.Model):

    __tablename__ = "Owner"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    puppy_id = db.Column(db.Integer, db.ForeignKey('Puppies.id'))
    puppy = db.relationship('Puppies', back_populates='owners')