from flask import Blueprint, render_template, request, redirect
from . import models

bp = Blueprint(
    'reptile',
    __name__,
    url_prefix="/reptiles"
)

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form:
            print("using form")
            common_name = request.form['common_name'],
            scientific_name = request.form['scientific_name'],
            conservation_status = request.form['conservation_status'],
            native_habitat = request.form['native_habitat'],
            fun_fact = request.form['fun_fact']
        else:
            print("Using headers")
            common_name = request.headers['common_name']
            scientific_name = request.headers['scientific_name']
            conservation_status = request.headers['conservation_status']
            native_habitat = request.headers['native_habitat']
            fun_fact = request.headers['fun_fact']

        # Create
        new_reptile = models.Reptile(
            common_name=common_name,
            scientific_name=scientific_name,
            conservation_status=conservation_status,
            native_habitat=native_habitat,
            fun_fact=fun_fact)
        # Add
        models.db.session.add(new_reptile)
        # Commit
        models.db.session.commit()
        return redirect('/reptiles')
    else:
        # GET 
        # find all reptiles 
        found_reptiles = models.Reptile.query.all()

        # create empty dictionary with an empty list value
        reptile_dict = {'reptiles': []}

        # loop through all reptiles and append it to the list 
        for reptile in found_reptiles:
            reptile_dict["reptiles"].append({
                'common_name': reptile.common_name,
                'scientific_name': reptile.scientific_name,
                'conservation_status': reptile.conservation_status,
                'native_habitat': reptile.native_habitat,
                'fun_fact': reptile.fun_fact
            })

        # return the dictionary, which will get returned as JSON by default
        return reptile_dict

@bp.route('/<int:id>')
def show(id): 
    # find the reptile by id
    reptile = models.Reptile.query.filter_by(id=id).first()

    if reptile:
        # create a dictionary of the reptile's information
        reptile_dict = {
            'common_name': reptile.common_name,
            'scientific_name': reptile.scientific_name,
            'conservation_status': reptile.conservation_status,
            'native_habitat': reptile.native_habitat,
            'fun_fact': reptile.fun_fact
        }
        
        # return the dictionary, which will get returned as JSON by default
        return reptile_dict
    else:
        return "Not Found"