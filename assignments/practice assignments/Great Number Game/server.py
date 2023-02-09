from flask import Flask, render_template, session, redirect,request
import random 
app = Flask(__name__)
app.secret_key = 'counter strike' 

@app.route('/')     
def index():
    if('count' not in session):
        session['count']=0
    if('num' not in session):
        session['num']=random.randint(1, 100)
    return render_template('index.html')

@app.route('/checkout',methods=['POST'])
def check():
    session['guess'] = int(request.form['guessed_number'])
    return redirect('/')
    
@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')
    
if __name__=="__main__":
    app.run(debug=True)

""" app.run(debug=True)     
ran=random.randint(1, 100)
if(int(request.form['guessed_number'])==ran):
    comment='your guess is right '
elif(int(request.form['guessed_number'])>ran):
    comment='Too high'
elif(int(request.form['guessed_number'])<ran):
    comment='Too Low'
return render_template('index.html', comment=comment) """