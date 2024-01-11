from flask import Flask, jsonify, request, make_response, abort
from flask_restful import reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api_database.db'
db = SQLAlchemy(app)

class Books(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50),nullable = False)
    author = db.Column(db.String(50), nullable=False)
    
    def json(self):
        return {'id': self.id,'title': self.title, 'author': self.author}
    
# db.create_all()

#Adding arguments for update/put method
book_update_args = reqparse.RequestParser()
book_update_args.add_argument("id", type=int, help="Name of the book is required")
book_update_args.add_argument("title", type=str, help="Title of the book")
book_update_args.add_argument("author", type=str, help="Author of the book")

#Get all books
@app.route('/books', methods=['GET'])
def get_all_books():
    books = Books.query.all()
    
    if not books:
        return {'Error':'Books Not Found'}
    
    return make_response(jsonify([book.json() for book in books]), 200)

#Get a specific book by it's id
@app.route('/books/<int:id>',methods=['GET'])
def get_book(id):
    books = Books.query.filter_by(id=id).first()
    if not books:
        return {'error':'Book does not exist with this id'}
    return make_response({
        "id" : books.id,
        "title": books.title,
        "author": books.author
            
    })

# #Creating a new Book
@app.route('/books/<int:id>',methods=['POST'])
def create_book(id):
    books = Books.query.filter_by(id=id).first()
    
    if books:
        return {'data':'Book already exists'}
    
    data = request.get_json()
    new_book = Books(id = data['id'], title = data['title'], author = data['author'])
    
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message':'Book Created Successfully'})
    
# #Updating a specific book by it's id
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    args = book_update_args.parse_args()
    result = Books.query.filter_by(id=id).first()
    if not result:
        abort(404, message="Book doesn't exist, cannot update")

    if args['id']:
        result.id = args['id']
    if args['title']:
        result.title = args['title']
    if args['author']:
        result.author = args['author']

    db.session.commit()

    return jsonify({'message':'Book updated Successfully'})

# #Deleting a specific book by it's id
@app.route('/books/<int:id>',methods=['DELETE'])
def delete_book(id):
    books = Books.query.filter_by(id=id).first()
    
    db.session.delete(books)
    db.session.commit()
    
    if not books:
        return {'error':'Book Not Found'}
    
    return {'data':'Book deleted successfully'}
    
if __name__ == '__main__':
    app.run(debug=True)