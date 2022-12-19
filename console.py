import pdb
from models.author import Author
from models.book import Book
from models.author_book import AuthorBook

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository
import repositories.author_book_repository as ab_repository


book_1=Book("Game Of Thrones 1","Story about thrones",14,3,7,"Fantasy")
book_1_results=book_repository.save(book_1)

book_2=Book("Harry Potter and the Philosophers Stone","Wizards",9,4,6,"Fantasy")
book_2_results=book_repository.save(book_2)

book_3=Book("Harry Potter and the Chamber of Secrets","Wizards",16,7,11,"Fantasy")
book_3_results=book_repository.save(book_3)

author_1=Author("George R.R","Martin",74)
author_1_results=author_repository.save(author_1)

author_2=Author("J.k","Rowling",57)
author_2_results=author_repository.save(author_2)

ab_1=AuthorBook(author_1,book_1)
ab_1_results=ab_repository.save(ab_1)

ab_2=AuthorBook(author_2,book_2)
ab_2_results=ab_repository.save(ab_2)

ab_3=AuthorBook(author_2,book_3)
ab_3_results=ab_repository.save(ab_3)

# Select all methods

select_all_books=book_repository.select_all()
select_all_authors=author_repository.select_all()
select_all_ab=ab_repository.select_all()
# for row in select_all_ab:
#     print(row.__dict__)

# Select single method

select_book=book_repository.select(book_2.id)
# print(select_book.__dict__)

select_author=author_repository.select(author_2.id)
# print(select_author.__dict__)
select_ab=ab_repository.select(ab_2.id)
print(select_ab.__dict__)
