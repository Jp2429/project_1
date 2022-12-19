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