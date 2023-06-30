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
            return jsonify(book_list)
    if request.method == 'POST':
        if len(request.form) == 2:
            title = request.form['title']
            author = request.form['author']
            id = book_list[-1]['id'] + 1
        if title and author:
            book_list.append({'id':id,'title':title,'author':author})
            return jsonify(book_list), 201
        else:
            return jsonify({'message': f'Required 2 paramters got {len(request.form)}'}), 404
        
            
    
