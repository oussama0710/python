from flask import Flask, render_template, request, redirect 
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
from user_model import User

#* ============ Display Route ============
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def all_users():
    all_users = User.get_all()
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
    User.save(data)
    # ---- alternative method since the request.form is already a dictionary -----
    # movie_id = Movie.save(request.form)

    return redirect('/')


if __name__=="__main__": 
    app.run(debug=True)  
