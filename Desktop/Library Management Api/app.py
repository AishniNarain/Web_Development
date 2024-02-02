from flask import Flask, jsonify, request, make_response, abort
from flask_sqlalchemy import SQLAlchemy
from flask_restful import reqparse
from datetime import datetime, timedelta
from twilio.rest import Client
import keys

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_BINDS'] = {  'fine' : 'sqlite:///fine.db',
                                    'users' : 'sqlite:///users.db',
                                    'borrow': 'sqlite:///borrow.db',
                                    'return': 'sqlite:///return.db'
                                }
db = SQLAlchemy(app)

class Books(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50),nullable = False)
    author = db.Column(db.String(50), nullable=False)
    edition = db.Column(db.String(50), nullable=False)
    
    def json(self):
        return {'id': self.id,'title': self.title, 'author': self.author, 'edition':self.edition}

class User(db.Model):
    __bind__key = 'users'
    
    id =db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable = False)
    username = db.Column(db.String(50),unique=True, nullable= False)
    department = db.Column(db.String(50), nullable=False)
    contact = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime)
    
    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'department': self.department,
            'contact': self.contact,
            'gender' : self.gender,
            'date' : self.date
        }
        
class Borrow(db.Model):
    __bind__key = 'borrow'
    
    id =db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50),nullable = False)
    book_title = db.Column(db.String(50), nullable=False)
    issue_date = db.Column(db.Date)
    token_no = db.Column(db.String(50), nullable=False)
    due_date = db.Column(db.Date)
    rel = db.relationship('Fine', backref='borrow')
    
    def json(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'book_title': self.book_title,
            'issue_date': self.issue_date,
            'token_no' : self.token_no,
            'due_date' : self.due_date
        }

class Fine(db.Model):
    __bind__key = 'fine'
    
    id = db.Column(db.Integer, primary_key = True)
    status = db.Column(db.String(50),nullable = False)
    fine = db.Column(db.Integer, nullable = False)
    borrow_id = db.Column(db.Integer, db.ForeignKey('borrow.id'))
    
    def json(self):
        return {
            'id': self.id,
            'status': self.status,
            'fine': self.fine
        }
    
class Return(db.Model):
    __bind__key = 'return'
    
    id =db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50))
    book_title = db.Column(db.String(50))
    issue_date = db.Column(db.Date)
    expected_return_date = db.Column(db.Date)
    charges = db.Column(db.Integer)
    
    def json(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'book_title': self.book_title,
            'issue_date': self.issue_date,
            'expected_return_date': self.expected_return_date,
            'charges' : self.charges
        }
        
#Adding arguments for update/put method
book_update_args = reqparse.RequestParser()
book_update_args.add_argument("id", type=int, help="Name of the book is required")
book_update_args.add_argument("title", type=str, help="Title of the book")
book_update_args.add_argument("author", type=str, help="Author of the book")

#Get all users
@app.route('/users',methods=['GET'])
def get_all_users():
    users = User.query.all()
    
    if not users:
        return {'error':'Users Not Found'}

    return make_response(jsonify([user.json() for user in users]), 200)

#Get a specific user by it's id
@app.route('/users/<int:id>',methods=['GET'])
def get_user(id):
    users = User.query.filter_by(id=id).first()
    
    if not users:
        return {'error':'User does not exist with this id'}
    
    return make_response({
            'id': users.id,
            'name': users.name,
            'username': users.username,
            'department': users.department,
            'contact': users.contact,
            'gender' : users.gender,
            'date' : users.date
    })

#Creating a new user
@app.route('/users',methods=['POST'])
def create_user():
    users = User.query.all()
    
    data = request.get_json()
    
    existing_user = User.query.filter_by(username=data['username']).first()
    if existing_user:
        return jsonify({"message": "Username already exists. Choose a different username"}), 400
    
    
    date1 = datetime.strptime(data['date'], '%Y-%m-%d')
    new_user = User(id= data['id'],name = data['name'],username= data['username'],department = data['department'],contact = data['contact'],gender = data['gender'],date = date1)

    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message':'User added successfully'})

#Get all books
@app.route('/books', methods=['GET'])
def get_all_books():
    books = Books.query.all()
    
    if not books:
        return {'Error':'Books Not Found'}
    
    return make_response(jsonify([book.json() for book in books]), 200)

# #Creating a new Book
@app.route('/books',methods=['POST'])
def create_book():
    books = Books.query.all()
    
    data = request.get_json()
    new_book = Books(id = data['id'], title = data['title'], author = data['author'], edition = data['edition'])
    
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
    
    if not books:
        return {'error':'Book Not Found'}
    
    db.session.delete(books)
    db.session.commit()
    
    return {'data':'Book deleted successfully'}

#Borrow book details
@app.route('/borrow_book', methods=['GET'])
def borrow_details():
    details = Borrow.query.all()
    
    if not details:
        return {"error":"No user's borrow details found"}
    
    return make_response(jsonify([detail.json() for detail in details]), 200)
    

add_days = timedelta(days=15)
#Creating Borrow Book Details
@app.route('/borrow_book',methods=['POST'])
def borrow_book():
    data = request.get_json()
    
    book1 = db.session.query(Books.title).all()
    book2 = data['book_title']
    
    existing_user = db.session.query(User.username).all()
    x = [x[0] for x in existing_user]
    if data['user_name'] not in x:
        return jsonify({"message": "User does not exist"}), 400
    
    x = [x[0] for x in book1]
    if book2 not in x:
        return jsonify({'message':'Book Unavailable'})
    
    existing_borrower = Borrow.query.filter_by(user_name = data['user_name']).first()
    if existing_borrower:
        return jsonify({"message": "User already exists, cannot borrow other book"}), 400
    
    date1 = datetime.strptime(data['issue_date'], '%Y-%m-%d')
    date2 = date1+ add_days
    
    new_details = Borrow(id = data['id'], user_name = data['user_name'],book_title = data['book_title'],issue_date= date1,token_no = data['token_no'],due_date = date2)
    
    db.session.add(new_details)
    db.session.commit()
    
    return jsonify({'message':'Borrow Book Details Created Successfully'})


#Displaying Borrow details of particular person
@app.route('/borrow_book/<int:id>',methods=['GET'])
def details(id):
    details = Borrow.query.filter_by(id=id).first()
    
    if not details:
        return {'error':'Borrow book details does not exist with this id'}
    
    return make_response({
            'id': details.id,
            'user_name': details.user_name,
            'book_title': details.book_title,
            'issue_date': details.issue_date,
            'token_no' : details.token_no,
            'due_date' : details.due_date
    })
    
#Displaying status and fine details of the borrower
@app.route('/borrow_book/<int:id>/fine',methods=['GET'])
def status_and_fine(id):
    details = Fine.query.filter_by(id=id).first()
    
    if not details:
        return {'error':'Details does not exist with this id'}
    
    return make_response({
            'id': details.id,
            'status': details.status,
            'fine': details.fine
    })
    
def calculate_fine(date1, due_date):
    days = (date1-due_date).days
    
    if (days >0 and days <=5):
        fine = (days*0.50)
    elif (days >= 6 and days <= 10):
        fine = (days*1)
    elif (days >10 and days <=30):
        fine = (days*5)
    else:
        fine = 0
        
    return fine

def message(status,date,number):
    
    client = Client(keys.account_sid, keys.auth_token)
    if status == 'Not Due':
        message = client.messages.create(
            body = "Your due date is "+date+ ".Kindly return your book on time",
            from_ = keys.twilio_number,
            to = number
        )
        return message.body
    
    elif status == 'Not Returned':
        message = client.messages.create(
            body = "Your due date has been exceeded, Thus fine will be calculated as per rate for overdue days",
            from_ = keys.twilio_number,
            to = keys.target_number
        )
        return message.body
    
    else:
        return "No updates"

#Calculating and displaying fine and status of the borrower
@app.route('/borrow_book/<int:id>/fine', methods =['POST'])
def calculate_status_and_fine(id):
    details = Borrow.query.filter_by(id=id).first()
    
    borrower_id = db.session.query(Borrow.id).first()
    
    if id not in borrower_id:
        return jsonify({'message':'Invalid user'})
    
    else:
        dt = User.query.filter_by(username = details.user_name).first()
        number = dt.contact
        due_date = details.due_date
        current_date = datetime.now().date()
        
        if current_date > due_date:
            status = "Not Returned"
            fine = calculate_fine(current_date, due_date)
            message(status,due_date,number)
            
        elif current_date == due_date:
            status = "Due date to return"
            fine = 0
            
        else:
            status = "Not Due"
            fine = 0
            message(status,due_date,number)
        
        details = Fine(id = id, status = status, fine = fine, borrow_id = id)
        
        db.session.add(details)
        db.session.commit()
        
        return jsonify({'message':'Details Created Successfully'})
    
#Return Book Details of a particular user
@app.route('/return_book/<int:id>/details', methods=['GET'])
def return_and_fine_details(id):
    details = Return.query.filter_by(id=id).first()
    
    if not details:
        return {'error':'No return book details found'}
    
    return make_response({
        'id': details.id,
        'user_name': details.user_name,
        'book_title': details.book_title,
        'issue_date': details.issue_date,
        'expected_return_date': details.expected_return_date,
        'charges' : details.charges
    })
    
#Return Book Details
@app.route('/return_book',methods=['GET'])
def return_book_details():
    return_details = Return.query.all()
    
    if not return_details:
        return {'error':'No return book details found'}
    
    return make_response(jsonify([return_detail.json() for return_detail in return_details]))
    
#Creating Return Book Details
@app.route('/return_book/<int:id>/details',methods=['POST'])
def return_book(id):
    details = Borrow.query.filter_by(id=id).first()
    if not details:
        return {'error':'Invalid User'}
    id = details.id
    user_name = details.user_name
    book_title = details.book_title
    issue_date = details.issue_date
    expected_return_date = details.due_date
    
    detail = Fine.query.filter_by(borrow_id=id).first()
    charges = detail.fine
    
    data = Return(id = id,user_name= user_name,book_title = book_title, issue_date = issue_date, expected_return_date = expected_return_date, charges=charges)
    
    db.session.add(data)
    db.session.commit()
    
    return jsonify({'message':'Return Book Details Created Successfully'})


if __name__ == '__main__':
    app.run(debug=True)