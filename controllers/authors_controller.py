from flask import Flask, render_template, redirect, request, Blueprint
from models.book import Book
from models.author import Author

from repositories import book_repository
from repositories import author_repository

authors_blueprint = Blueprint("authors", __name__)

# select all books
@authors_blueprint.route("/authors")
def index():
    authors = author_repository.select_all()
    return render_template("authors/index.html", all_authors=authors)