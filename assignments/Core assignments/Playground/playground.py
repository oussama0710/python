from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__) 

@app.route('/play')  
def play():
    return render_template("boxes.html")
@app.route('/play/<num>')  
def play2(num):
    return render_template("boxes.html",num=int(num))
@app.route('/play/<num>/<color>')  
def play3(num,color):
    return render_template("boxes.html",num=int(num),color=color)
if __name__=="__main__":
    app.run(debug=True) 
