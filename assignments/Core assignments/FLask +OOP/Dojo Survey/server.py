from flask import Flask, render_template, session, redirect,request
app = Flask(__name__)
app.secret_key = 'counter strike'

@app.route('/')     
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def index1():
    session['info']={}
    session['info']['Name']=request.form['Name']
    session['info']['Location']=request.form['location']
    session['info']['Programming']=request.form['language']
    session['info']['comments']=request.form['comments']
    return render_template('second_page.html',info=session['info'] )

if __name__=="__main__":    
    app.run(debug=True)     