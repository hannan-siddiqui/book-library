from flask import Flask, jsonify, request
from book_library import Library, Book

app = Flask(__name__)


library = Library()

@app.route('/add_book', methods=['POST'])
def add_book():
    data = request.json
    new_book = Book(data['title'], data['author'], data['isbn'], data['publication_year'])
    library.add_book(new_book)
    return jsonify({'message': 'Book added successfully'}), 200

@app.route('/borrow_book/<isbn>', methods=['PUT'])
def borrow_book(isbn):
    if library.borrow_book(isbn):
        return jsonify({'message': 'Book borrowed successfully'}), 200
    else:
        return jsonify({'message': 'Book is not available'}), 400

@app.route('/return_book/<isbn>', methods=['PUT'])
def return_book(isbn):
    library.return_book(isbn)
    return jsonify({'message': 'Book returned successfully'}), 200

@app.route('/search', methods=['GET'])
def search_books():
    title = request.args.get('title')
    author = request.args.get('author')
    publication_year = request.args.get('publication_year')
    results = library.search_books(title, author, publication_year)
    books_info = [{'title': book.title, 'author': book.author, 'isbn': book.isbn, 'publication_year': book.publication_year, 'status': book.status} for book in results]
    return jsonify(books_info), 200

if __name__ == '__main__':
    app.run(debug=True)