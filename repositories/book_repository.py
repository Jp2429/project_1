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