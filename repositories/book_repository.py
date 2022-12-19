from db.run_sql import run_sql

from models.book import Book
from models.author import Author

def save(book):
    sql="INSERT INTO books(title,description,stock_quantity,buying_cost,selling_price,genre) VALUES(%s,%s,%s,%s,%s,%s)RETURNING *"
    values= [book.title,book.description,book.stock_quantity,book.buying_cost,book.selling_price,book.genre]
    query_results=run_sql(sql,values)
    id =query_results[0]['id']
    book.id=id
    return book

def select_all():
    books = []
    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        book = Book(row['title'],row['description'],row['stock_quantity'],row['buying_cost'],row['selling_price'],row['genre'] , row['id'])
        books.append(book)
    return books

def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]

    if results is not None:
        book = Book(results['title'],results['description'],results['stock_quantity'],results['buying_cost'],results['selling_price'],results['genre'] , results['id'])
    return book