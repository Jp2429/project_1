from db.run_sql import run_sql

from models.book import Book
from models.author import Author

def save(author):
    sql="INSERT INTO author (first_name,last_name,age) VALUES (%s,%s,%s)"
    values=[author.first_name,author.last_name,author.age]
    query_results=run_sql(sql,values)
    id =query_results[0]['id']
    author.id=id
    return author