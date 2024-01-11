from flask import Flask,jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

books = [
    {'id':1, 'title':'Book 1', 'author': 'Author 1'},
    {'id':2, 'title':'Book 2', 'author': 'Author 2'},
    {'id':3, 'title':'Book 3', 'author': 'Author 3'},
]


#Get all the books
@app.route('/books',methods=['GET'])
def get_books():
    return books  

#Get a specific book by it's id
@app.route('/books/<int:book_id>',methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return book
    return {'error':'Book Not Found'}

#Creating a new Book
@app.route('/books',methods=['POST'])
def create_book():
    new_book = {'id': len(books)+1, 'title': request.json['title'], 'author': request.json['author']}
    books.append(new_book)
    return new_book

#Updating a specific book by it's id
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book['id'] == book_id:
            book['title'] = request.json['title']
            book['author'] = request.json['author']
            return book
    return {'error':'Book Not Found'}

#Deleting a specific book by it's id
@app.route('/books/<int:book_id>',methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {'data':'Book deleted successfully'}
    return {'error':'Book Not Found'}
    
if __name__ == '__main__':
    app.run(debug=True)