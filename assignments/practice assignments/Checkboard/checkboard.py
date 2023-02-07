from flask import Flask, render_template
app = Flask(__name__) 

@app.route('/')  
def initial():
    return render_template("checkboard.html")
@app.route('/<num>')
def second(num):
    return render_template("checkboard.html", num=int(num))
@app.route('/<x>/<y>')
def third(x,y):
    return render_template("checkboard.html", num=int(x),y=int(y))
if __name__=="__main__":
    app.run(debug=True)
