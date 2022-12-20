from flask import Flask, render_template, redirect, request, Blueprint
from models.book import Book
from models.author import Author
from models.author_book import AuthorBook

from repositories import book_repository
from repositories import author_repository 
from repositories import author_book_repository as ab_repository

ab_blueprint = Blueprint("ab", __name__)

# select all author_book
@ab_blueprint.route("/ab")
def index():
    all_ab = ab_repository.select_all()
    return render_template("ab/index.html", all_ab=all_ab)

# GET author_book
@ab_blueprint.route("/ab/new", methods=['GET'])
def new_task():
    authors = author_repository.select_all()
    books = book_repository.select_all()
    return render_template("ab/new.html", authors = authors, books = books)

# CREATE
@ab_blueprint.route("/ab",  methods=['POST'])
def create_ab():
    author_id = request.form['author_id']
    book_id = request.form['book_id']
    print (book_id)
    authors = author_repository.select(author_id)
    books = book_repository.select(book_id)
    ab = AuthorBook(authors, books)
    ab_repository.save(ab)
    return redirect('/ab')