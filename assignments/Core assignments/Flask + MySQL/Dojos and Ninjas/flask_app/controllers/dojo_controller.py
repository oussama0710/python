from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo_model

@app.route('/')
def show_dojo():
    all_dojos = dojo_model.Dojo.get_all()
    return render_template('new_dojo.html',all_dojos=all_dojos)

@app.route('/create/dojo', methods=['POST'])
def add_dojo():
    data = {
        "name": request.form["name"],
        }
    dojo_model.Dojo.add_dojo(data)
    return redirect('/')

@app.route('/dojo/<int:id>')
def show_dojo_ninjas(id):
    data = {
        "id": id
    }
    return render_template('dojo_ninjas.html', dojo=dojo_model.Dojo.join_dojo(data))