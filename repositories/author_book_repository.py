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