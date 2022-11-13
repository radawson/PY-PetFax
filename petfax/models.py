from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Fact(db.Model):
    __tablename__ = 'facts'

    id = db.Column(db.Integer, primary_key = True)
    submitter = db.Column(db.String(250))
    fact = db.Column(db.Text)

class Reptile(db.Model):
    __tablename__ = 'reptiles'

    id = db.Column(db.Integer, primary_key = True)
    common_name = db.Column(db.String(250))
    scientific_name = db.Column(db.String(250))
    conservation_status = db.Column(db.String(250))
    native_habitat = db.Column(db.Text)
    fun_fact = db.Column(db.Text)
