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

def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(book):
    sql = "UPDATE books SET (title,description,stock_quantity,buying_cost,selling_price,genre) = (%s,%s,%s,%s,%s,%s) WHERE id = %s"
    values= [book.title,book.description,book.stock_quantity,book.buying_cost,book.selling_price,book.genre,book.id]
    run_sql(sql, values)

#Pleased with this

def markup(id):
    book=None
    sql="SELECT * FROM books WHERE id=%s"
    values=[id]
    results=run_sql(sql,values)[0]

    if results is not None:
        book=Book(results['title'],results['description'],results['stock_quantity'],results['buying_cost'],results['selling_price'],results['genre'] , results['id'])
        profit=book.selling_price-book.buying_cost
        percentage=profit/book.buying_cost
        markup=percentage*100
        rounded=round(markup,2)
    return rounded

def filter_author(input_id):
    books=[]
    sql="SELECT books.* FROM books INNER JOIN authorsBooks ON authorsBooks.book_id=books.id WHERE author_id=%s"
    values=[input_id]
    results=run_sql(sql,values)

    for row in results:
        book = Book(row['title'],row['description'],row['stock_quantity'],row['buying_cost'],row['selling_price'],row['genre'] , row['id'])
        books.append(book)
    return books
