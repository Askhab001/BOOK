from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

books = []


class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "price": self.price,
            "stock": self.stock
        }


@app.route('/')
def index():
    return render_template('book.html', books=books)


@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    price = float(request.form['price'])
    stock = int(request.form['stock'])

    new_book = Book(title, author, price, stock)
    books.append(new_book)

    return redirect(url_for('index'))


@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify([book.to_dict() for book in books])


@app.route('/api/books/<string:title>', methods=['GET'])
def get_book(title):
    for book in books:
        if book.title.lower() == title.lower():
            return jsonify(book.to_dict())
    return jsonify({"error": "Book not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
