from flask import Flask,request,jsonify

app = Flask(__name__)

book_list = [
    {'id': 1,'title': 'Things fall apart','author':'Chinua Achebe'},
    {'id': 2,'title': 'Poor dad Rich dad','author':'John Neeman'},
    ]

@app.route('/books',methods=['GET','POST'])
def books():
    if request.method == 'GET':
        if request.args:
            id = int(request.args.get('id'))
            if id is not None and id != 0:
                try:
                    return jsonify({'data': book_list[id -1],'status':'success'})
                except:
                    return jsonify({'message': 'Id specified does not exist', 'status': 'Failed'})
            elif id == 0:
                return jsonify({'message': 'Id specified does not exist', 'status': 'Failed'})
            else:
                return jsonify({'message': 'Did not specify an ID', 'status': 'Failed'})
        else:
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
@app.route('/books/<int:id>',methods=['GET','PUT','DELETE'])
def book(id):
    if request.method == 'GET':
        if id != 0:
            try:
                return jsonify({'data': book_list[id -1],'status':'success'})
            except:
                return jsonify({'message': 'Id specified does not exist', 'status': 'Failed'})
        else:
            return jsonify({'message': 'Id specified does not exist', 'status': 'Failed'})
        
            
    
