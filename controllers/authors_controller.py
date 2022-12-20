from flask import Flask, render_template, redirect, request, Blueprint
from models.book import Book
from models.author import Author

from repositories import book_repository
from repositories import author_repository

authors_blueprint = Blueprint("authors", __name__)

# select all authors
@authors_blueprint.route("/authors")
def index():
    authors = author_repository.select_all()
    return render_template("authors/index.html", all_authors=authors)

#select one author
@authors_blueprint.route("/authors/<id>")
def show_book(id):
    author=author_repository.select(id)
    return render_template("/authors/show_author.html",author=author)

# delete
@authors_blueprint.route("/authors/<id>/delete", methods=['POST'])
def destroy(id):
    author_repository.delete(id)
    return redirect ("/authors")

# new author
@authors_blueprint.route("/authors/new_author")
def new_author():
    return render_template("authors/new_author.html")


# create author
@authors_blueprint.route("/authors", methods=['POST'])
def create_author():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    age = request.form['age']
    active = True if 'active' in request.form else False
    author = Author(first_name,last_name,age,active)
    author_repository.save(author)
    return redirect('/authors')

# edit author
@authors_blueprint.route("/authors/<id>/edit_author")
def edit(id):
    author = author_repository.select(id)
    return render_template("/authors/edit_author.html", author=author)


# update book
@authors_blueprint.route("/authors/<id>/edit_author", methods=['POST'])
def update(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    age = request.form['age']
    active = True if 'active' in request.form else False
    author = Author(first_name,last_name,age,active,id)
    author_repository.update(author)
    return redirect('/authors')