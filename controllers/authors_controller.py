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

@authors_blueprint.route("/authors/<id>")
def show_book(id):
    author=author_repository.select(id)
    return render_template("/authors/show_author.html",author=author)

# delete
@authors_blueprint.route("/authors/<id>/delete", methods=['POST'])
def destroy(id):
    author_repository.delete(id)
    return redirect ("/authors")