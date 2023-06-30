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
        title = request.method['title'] or None
        author = request.method['author'] or None
        id = book_list[-1]['id'] + 1
        if title is not None and author is not None:
            book_list.append({'id':id,'title':title,'author':author})
            return jsonify(book_list), 201
        elif title is None:
            return jsonify({'message': 'Title not specified'}), 404
        elif author is None:
            return jsonify({'message': 'Author not specified'}), 404
        
        
            
    
