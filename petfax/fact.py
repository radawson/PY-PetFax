from flask import Blueprint, render_template, request, redirect
from . import models

bp = Blueprint(
    'fact',
    __name__,
    url_prefix="/facts"
)

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        submitter = request.form['submitter']
        fact = request.form['fact']

        # Create
        new_fact = models.Fact(submitter=submitter, fact=fact)
        # Add
        models.db.session.add(new_fact)
        # Commit
        models.db.session.commit()

        return redirect('/facts')
    else:
        results = models.Fact.query.all()
        #print(results)
        return render_template('facts/index.html', facts=results)
    

@bp.route('/new')
def new(): 
    return render_template('facts/new.html')