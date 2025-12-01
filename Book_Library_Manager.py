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

import json
import sys
import csv

# -------------------------
# კლასი BOOK
# -------------------------
class Book:
    counter = 0

    def __init__(self, title, author, genre, publication_year, book_id=None):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year
        
        if book_id is not None:
            self.book_id = book_id
        else:
            Book.counter += 1
            self.book_id = Book.counter

    def __str__(self):
        return f"ID: {self.book_id} | Title: {self.title} | Author: {self.author} | Genre: {self.genre} | Year: {self.publication_year}"
    
    def to_dict(self):
        return {
            'book_id': self.book_id,
            'title': self.title,
            'author': self.author,
            'genre': self.genre,
            'publication_year': self.publication_year
        }

# -------------------------
# კლასი LIBRARY
# -------------------------
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, genre, publication_year):

        for book in self.books:
            if book.title.lower() == title.lower() and \
                book.author.lower() == author.lower():
                print(f"❌ Book '{title}' by '{author}' already exists in the library.")
                return False
            
        new_book = Book(title, author, genre, publication_year)
        self.books.append(new_book)
        print(f"✅ Book '{title}' added to the library (ID: {new_book.book_id}).")
        return True

    def view_all_books(self):
        if not self.books:
            print("❌ Library is empty.")
            return
        
        print("\n--- All Books ---")
        for book in self.books:
            print(book)
    
    def search_book(self, search_term):
        found_books = []
        search_term_lower = search_term.lower()

        for book in self.books:
            if (search_term_lower in book.title.lower() or
                search_term_lower in book.author.lower() or
                search_term_lower in book.genre.lower()):
                found_books.append(book)

        if not found_books:
            print(f"\n❌ Book(s) with the term '{search_term}' not found.")
        else:
            print(f"\n✅ Found {len(found_books)} book(s):")
            for book in found_books:
                print("-" * 40)
                print(book)
                print("-" * 40)


    def remove_book(self, book_id):
        try:
            target_id = int(book_id)
        except ValueError:
            print("❌ ID must be a number.")
            return
        
        for book in self.books:
            if book.book_id == target_id:
                self.books.remove(book)
                print(f"✅ Book '{book.title}' removed from the library.")
                return
        print(f"❌ No book found with ID {book_id}.")

    def update_book(self, book_id):
        try:
            target_id = int(book_id)
        except ValueError:
            print("❌ ID must be a number.")
            return
        
        for book in self.books:
            if book.book_id == target_id:
                print("\n--- Update Book ---")
                new_title = input(f"Enter new title (Old: '{book.title}'): ").strip()
                new_author = input(f"Enter new author (Old: '{book.author}'): ").strip()
                new_genre = input(f"Enter new genre (Old: '{book.genre}'): ").strip()
                new_year = input(f"Enter new publication year (Old: '{book.publication_year}'): ").strip()

                if new_title:
                    book.title = new_title
                if new_author:
                    book.author = new_author
                if new_genre:
                    book.genre = new_genre

                if new_year:
                    try:
                        new_year = int(new_year)
                        if 0 <= new_year <= 2025:
                            book.publication_year = new_year
                            
                        else:
                            print("⚠️ Invalid year: must be between 0 and 2025.")
                    except ValueError:
                        print("⚠️ Year not updated: Please enter a valid number.")
                print(f"✅ Book ID {book_id} updated successfully.")
                return
                
        print(f"\n❌ No book found with ID {book_id}.")

    def save_data(self):
        list_of_dicts = [book.to_dict() for book in self.books]
        try:
            with open("library_data.json", "w", encoding='utf-8') as file:
                json.dump(list_of_dicts, file, indent=4)
            print("✅ Library data saved successfully in 'library_data.json'.")
        except Exception as e:
            print(f"❌ Error saving data: {e}")
    
    def save_data_csv(self):
        # ველების სახელები (CSV ფაილის სათაურის ხაზი)
        fieldnames = ['book_id', 'title', 'author', 'genre', 'publication_year']
        
        # წიგნების მონაცემების მიღება ლექსიკონების სახით
        list_of_dicts = [book.to_dict() for book in self.books]

        try:
            # ფაილის გახსნა 'w' (write) რეჟიმში
            with open("library_data.csv", "w", newline='', encoding='utf-8') as file:
                # DictWriter-ის შექმნა
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                
                # სათაურის (ჰედერების) ჩაწერა
                writer.writeheader()
                
                # მონაცემების ჩაწერა
                writer.writerows(list_of_dicts)
                
            print("✅ Library data successfully saved to 'library_data.csv'.")
        except Exception as e:
            print(f"❌ Error saving CSV data: {e}")

    def load_data(self):
        try:
            with open("library_data.json", "r", encoding='utf-8') as file:
                data = json.load(file)
            self.books = [Book(**book_dict) for book_dict in data]
            if self.books:
                Book.counter = max(int(book.book_id) for book in self.books)
            print("✅ Library data loaded successfully from 'library_data.json'.")
        except FileNotFoundError:
            print("Library data file not found. Starting with an empty library.")
        except Exception as e:
            print(f"❌ Error loading data: {e}")

# -------------------------
# მთავარი ფუნქცია (CLI)
# -------------------------
def main():
    library = Library() 
    library.load_data()

    while True:
        print("\n=== 📚 BOOK LIBRARY MANAGER 📚 ===")
        print("1️⃣  Add Book")
        print("2️⃣  View All Books")
        print("3️⃣  Search Book")
        print("4️⃣  Remove Book")
        print("5️⃣  Update Book")
        print("6️⃣  Save Data (JSON)")
        print("7️⃣  Load Data (JSON)")
        print("8️⃣  Save Data to CSV")
        print("9️⃣  Exit")
        choice = input("👉 Choose an option (1-9): ").strip()

        if choice == '1':
            print("\n📘 ADD NEW BOOK")
            title = input("Enter Title: ").strip()
            author = input("Enter Author: ").strip()
            genre = input("Enter Genre: ").strip()
            year = input("Enter Publication Year: ").strip()
            if not title or not author or not genre or not year:
                print("❌ Title, Author, and Year cannot be empty! Please try again!")
            else:

                try:
                    year = int(year)
                    library.add_book(title, author, genre, year)
                    library.save_data()
                    library.save_data_csv()
                except ValueError:
                    print("❌ Invalid year! Must be a number.")

        elif choice == '2':
            print("\n📚 ALL BOOKS IN LIBRARY")
            library.view_all_books()

        elif choice == '3':
            print("\n🔍 SEARCH BOOKS")
            term = input("Enter search term: ").strip()
            library.search_book(term)

        elif choice == '4':
            print("\n❌ REMOVE BOOK")
            book_id = input("Enter Book ID: ").strip()
            library.remove_book(book_id)

        elif choice == '5':
            print("\n✏️ UPDATE BOOK INFO")
            book_id = input("Enter Book ID: ").strip()
            library.update_book(book_id)

        elif choice == '6':
            print("\n💾 Saving data...")
            library.save_data()

        elif choice == '7':
            print("\n📂 Loading data...")
            library.load_data()

        elif choice == '8':
            print("\n📄 Saving CSV...")
            library.save_data_csv()

        elif choice == '9':
            print("\n👋 Exiting... Goodbye!")
            sys.exit()

        else:
            print("❌ Invalid choice. Enter a number 1-9.")


if __name__ == "__main__":
    main()