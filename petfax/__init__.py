from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Factory function
def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:password01@localhost:5432/petfax2'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route('/')
    def index():
        return "<H2>Hello, Welcome to PetFax.</H2>"

    from . import pet
    app.register_blueprint(pet.bp) 

    from . import fact
    app.register_blueprint(fact.bp) 

    from . import reptile
    app.register_blueprint(reptile.bp) 

    return app