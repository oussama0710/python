from flask import Flask 
app = Flask(__name__)    
@app.route('/')          
def hello_world():
    return 'Hello World!'
@app.route('/dojo')
def dojo():
    return 'Dojo!'
@app.route('/say/<name>')
def say(name):
    print(type(name))
    return (f'Hi {name} {type(name)}')
@app.route('/repeat/<num>/<str>')
def rep(num,str):
    return (f'{str*int(num)}')

if __name__=="__main__": 
    app.run(debug=True) 

