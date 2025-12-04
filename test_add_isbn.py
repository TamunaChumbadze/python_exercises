import requests # type: ignore
from book_library_manager import Library

library = Library()
library.load_data() 


isbn_list = [
    "9780141439518",  # Pride and Prejudice
    "9780451524935",  # 1984
    "9780743273565",  # The Great Gatsby
    "9780061120084",  # To Kill a Mockingbird
    "9781503280786"   # Moby-Dick
]

for isbn in isbn_list:
    print(f"\n📘 Adding ISBN: {isbn}")
    library.add_book_by_isbn(isbn)

library.save_all_data()

print("\n📚 Current books in library:")
library.view_all_books()