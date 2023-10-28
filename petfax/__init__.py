from flask import Flask

def create_app():
    app = Flask(__name__)


    # index route
    @app.route("/")
    def index():
        return "<h1>Welcome to PetFax!</h1>"


    # pets index route
    from . import pets
    app.register_blueprint(pets.bp) # route /pets
    
    return app