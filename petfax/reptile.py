from flask import Blueprint, redirect, render_template, request

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
            print("Using form")
            common_name = request.form['common_name']
            scientific_name = request.form['scientific_name']
            conservation_status = request.form['conservation_status']
            native_habitat = request.form['native_habitat']
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
                'db_id':reptile.id,
                'common_name': reptile.common_name,
                'scientific_name': reptile.scientific_name,
                'conservation_status': reptile.conservation_status,
                'native_habitat': reptile.native_habitat,
                'fun_fact': reptile.fun_fact
            })

        # return the dictionary, which will get returned as JSON by default
        return reptile_dict

@bp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def reptiles(id): 
    if request.method=='DELETE':
        reptile = models.Reptile.query.get(id)
        if reptile:
            models.db.session.delete(reptile)
            models.db.session.commit()
            return redirect('/reptiles')
        else:
            return "Not Found"
    elif request.method=='GET':
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
    elif request.method=='PUT':
        reptile = models.Reptile.query.get(id)
        if reptile:
            if request.form:
                print("Using form")
                print(request.form)
                if 'common_name' in request.form:
                    reptile.common_name = request.form['common_name']
                if 'scientific_name' in request.form:    
                    reptile.scientific_name = request.form['scientific_name']
                if 'conservation_status' in request.form:
                    reptile.conservation_status = request.form['conservation_status']
                if 'native_habitat' in request.form:
                    reptile.native_habitat = request.form['native_habitat']
                if 'fun_fact' in request.form:
                    reptile.fun_fact = request.form['fun_fact']            
            else:
                print("Using headers")
                if 'common_name' in request.headers:
                    reptile.common_name = request.headers['common_name']
                if 'scientific_name' in request.headers:
                    reptile.scientific_name = request.headers['scientific_name']
                if 'conservation_status' in request.headers:
                    reptile.conservation_status = request.headers['conservation_status']
                if 'native_habitat' in request.headers:
                    reptile.native_habitat = request.headers['native_habitat']
                if 'fun_fact' in request.headers:
                    reptile.fun_fact = request.headers['fun_fact']
            
            models.db.session.commit()
            return redirect('/reptiles')

        else:
            return "Not Found"
    else:
        return "unknown request"