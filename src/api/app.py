from flask import Flask, request, jsonify
from src.api.books_api import LibrioAPI

app = Flask(__name__)
api = LibrioAPI()

@app.route("/library", methods=['GET'])
def get_books():
    query =  request.args.get('q')
    if query:
        books = api.search_books(query)
        return jsonify([book.to_dict() for book in books])
    else:
        return jsonify({"error": "Missing query parameter q"}), 400
@app.route("/books/<book_id>", methods = ['GET'])
def get_book_info(book_id):
    book = api.get_book(book_id)
    return jsonify(book.to_dict())