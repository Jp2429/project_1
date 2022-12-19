from db.run_sql import run_sql

from models.book import Book
from models.author import Author

def save(author):
    sql="INSERT INTO authors (first_name,last_name,age,active) VALUES (%s,%s,%s,%s) RETURNING *"
    values=[author.first_name,author.last_name,author.age,author.active]
    query_results=run_sql(sql,values)
    id =query_results[0]['id']
    author.id=id
    return author

def select_all():
    authors = []
    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = Author(row['first_name'],row['last_name'],row['age'],row['active'], row['id'])
        authors.append(author)
    return authors

def select(id):
    author = None
    sql = "SELECT * FROM authors WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]
    if results is not None:
        author = Author(results['first_name'],results['last_name'],results['age'],results['active'], results['id'])
    return author

def delete_all():
    sql = "DELETE FROM authors"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM authors WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(author):
    sql = "UPDATE authors SET (first_name,last_name,age,active) = (%s, %s, %s,%s) WHERE id = %s"
    values=[author.first_name,author.last_name,author.age,author.id,author.active]
    run_sql(sql, values)