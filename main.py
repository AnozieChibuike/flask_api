from flask import Flask,request,jsonify

app = Flask(__name__)

book_list = [
    {'id': 1,'title': 'Things fall apart','author':'Chinua Achebe'},
    {'id': 2,'title': 'Poor dad Rich dad','author':'John Neeman'},
    ]

@app.route('/books',methods=['GET','POST'])
def books():
    if request.method == 'GET':
        if book_list:
            return jsonify({'data':book_list,'status':'success'})
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        id = book_list[-1]['id'] + 1
        if title is not None and author is not None:
            book_list.append({'id':id,'title':title,'author':author})
            return jsonify({'data': book_list,'message': 'Created Successfully', 'status': 'success'}), 201
        else:
            return jsonify({'message': 'Invalid params', 'status': 'Failed'}), 404
        
            
    
