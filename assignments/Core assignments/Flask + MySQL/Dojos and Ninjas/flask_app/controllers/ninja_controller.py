from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import ninja_model
from flask_app.models import dojo_model

@app.route('/ninjas')
def ninjas():
    
    return render_template('new_ninja.html',dojos= dojo_model.Dojo.get_all())

@app.route('/create/ninja', methods=['POST'])
def add_ninja():
    ninja_model.Ninja.add_ninja(request.form)
    return redirect('/')
