from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import user_model

#* ============ Display Route ============
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def all_users():
    all_users = user_model.User.get_all()
    print(all_users)
    return render_template("show_users.html",all_users=all_users)  # Return the string 'Hello World!' as a response


@app.route('/create')
def create_user():

    return render_template('create_user.html')

@app.route("/create/user", methods=['POST'])
def process_form():

    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form['last_name'],
        "email": request.form['email']
        }
    user_model.User.save(data)
    # ---- alternative method since the request.form is already a dictionary -----
    # movie_id = Movie.save(request.form)

    return redirect('/')

@app.route("/delete/user/<int:id>")
def delete(id):
    data = {"id":id}
    user_model.User.delete(data)
    # ---- alternative method since the request.form is already a dictionary -----
    # movie_id = Movie.save(request.form)

    return redirect('/')

@app.route('/user/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit_user.html",user=user_model.User.get_one(data))

@app.route('/user/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("show_user.html",user=user_model.User.get_one(data))

@app.route('/user/update',methods=['POST'])
def update():
    user_model.User.update(request.form)
    return redirect('/')