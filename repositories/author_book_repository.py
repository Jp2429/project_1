from db.run_sql import run_sql

from models.book import Book
from models.author import Author
from models.author_book import AuthorBook

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

def save(ab):
    sql="INSERT INTO authorsBooks(author_id,book_id) VALUES(%s,%s) RETURNING id"
    values=[ab.author.id,ab.book.id]
    query_results=run_sql(sql,values)
    id=query_results[0]['id']
    ab.id=id
    return ab

def select_all():
    abs=[]
    sql="SELECT * FROM authorsBooks"
    query_results=run_sql(sql)

    for row in query_results:
        author=author_repository.select(row['author_id'])
        book=book_repository.select(row['book_id'])
        ab= AuthorBook(author,book,row['id'])
        abs.append(ab)
    return abs


def select(id):
    ab = None
    sql = "SELECT * FROM authorBooks WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]

    if results is not None:
        author = author_repository.select(results['author_id'])
        book=book_repository.select(results['book_id'])
        ab = AuthorBook(author,book, results['id'])
    return ab
