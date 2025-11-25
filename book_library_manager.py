"""
Project Title: “Book Library Manager”
Project description: A Python application to manage a personal book library, allowing users to add, remove, search, and organize their book collection.
Functionality:
1. Add Books: Users can add new books to their library with details such as title, author, genre, and publication year.
2. Remove Books: Users can remove books from their library by title or author.
3. Search Books: Users can search for books by title, author, or genre.
4. Update Book Details: Users can update the details of existing books in their library.
5. Save Data: The application saves the book collection to a file and loads it upon startup.
6. Load Data: The application loads the book collection from a file when started.

"""

class Book:
    counter = 0

    def __init__(self, title, author, genre, publication_year, book_id=None):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year
       
        if book_id is not None: # თუ book_id გადმოცემულია, გამოვიყენოთ ის
            self.book_id = book_id
        else:
            Book.counter += 1 # ავტომატურად გავზარდოთ counter და მივანიჭოთ book_id
            self.book_id = Book.counter # ავტომატურად book_id-ის მინიჭება
            pass


        