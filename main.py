from flask import Flask

app = Flask(__name__)

@app.route('/books',methods=['GET','POST')
def books():
    
