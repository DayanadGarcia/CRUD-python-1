from crypt import methods
from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
  {
    'id': 1,
    'título': 'Ulisses',
    'autor': 'James Joyce'
  },
  {
    'id': 2,
    'título': 'Em Busca do Tempo Perdido',
    'autor': 'Marcel Proust'
  },
  {
    'id': 3,
    'título': 'A Montanha Mágica',
    'autor': 'Thomas Mann'
  },
  {
    'id': 4,
    'título': 'Guerra e Paz',
    'autor': 'Liev Tolstói'
  }
]

#GET all books
@app.route('/books', methods=['GET'])
def get_all_books():
  return jsonify(books)
  
#GET book by id
@app.route('/books/<int:id>', methods=['GET'])
def get_book_by_id(id):
  for book in books:
    if book.get('id') == id:
      return jsonify(book)

#UPDATE book by id
@app.route('/books/<int:id>', methods=['PUT'])
def update_book_by_id(id):
  updated_book = request.get_json()
  for index,book in enumerate(books):
    if book.get('id') == id:
      books[index].update(updated_book)
      return jsonify(books[index])

#POST new book
@app.route('/books', methods=['POST'])
def new_book():
  book = request.get_json()
  books.append(book)
  return jsonify(books)

#DELETE book by id
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book_by_id(id):
  for index, book in enumerate(books):
    if book.get('id') == id:
      del books[index]
  return jsonify(books)


app.run(port=5000, host='localhost', debug=True)