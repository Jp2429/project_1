from flask import Flask, render_template, redirect, request, Blueprint
from models.book import Book
from models.author import Author

from repositories import book_repository
from repositories import author_repository

books_blueprint = Blueprint("books", __name__)

# select all books
@books_blueprint.route("/books")
def index():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books=books)

@books_blueprint.route("/books/<id>")
def show_book(id):
    book=book_repository.select(id)
    markup=book_repository.markup(id)
    #TODO create a markup calculation method
    return render_template("/books/show_book.html",book=book,markup=markup)

# delete
@books_blueprint.route("/books/<id>/delete", methods=['POST'])
def destroy(id):
    book_repository.delete(id)
    return redirect ("/books")

# new book
@books_blueprint.route("/books/new_book")
def new_book():
    return render_template("books/new_book.html")


# create book
@books_blueprint.route("/books", methods=['POST'])
def create_book():
    title = request.form['title']
    genre = request.form['genre']
    description=request.form['description']
    stock_quantity=request.form['stock_quantity']
    buying_cost=request.form['buying_cost']
    selling_price=request.form['selling_price']
    book=Book(title,description,stock_quantity,buying_cost,selling_price,genre)
    book_repository.save(book)
    return redirect('/books')

# edit book
@books_blueprint.route("/books/<id>/edit_book")
def edit(id):
    book = book_repository.select(id)
    return render_template("/books/edit_book.html", book=book)


# update book
@books_blueprint.route("/books/<id>/edit_book", methods=['POST'])
def update(id):
    title = request.form['title']
    genre = request.form['genre']
    description=request.form['description']
    stock_quantity=request.form['stock_quantity']
    buying_cost=request.form['buying_cost']
    selling_price=request.form['selling_price']
    book = Book(title,description,stock_quantity,buying_cost,selling_price,genre,id)
    book_repository.update(book)
    return redirect('/books')