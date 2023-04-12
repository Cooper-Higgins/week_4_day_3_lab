import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author_1 = Author("Markus", "Zusak")
author_repository.save(author_1)
author_2 = Author("Rebecca", "Henderson")
author_repository.save(author_2)

author_repository.select_all()

book_1 = Book("The Book Thief", "Historical Fiction")
book_repository.save(book_1)

book_2 = Book("Reimagining Capitalism in a World on Fire", "Sustainability")
book_repository.save(book_2)


pdb.set_trace()