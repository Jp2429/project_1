import pdb
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository


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


# 