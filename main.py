from flask import Flask,request,jsonify

app = Flask(__name__)

book_list = [
    {'id': 1,'title': 'Things fall apart','author':'Chinua Achebe'},
    {'id': 2,'title': 'Poor dad Rich dad','autho':'John Neeman'},
    ]

@app.route('/books',methods=['GET','POST'])
def books():
    if request.method == 'GET':
        if book_list:
            return jsonify(book_list), 500
    
