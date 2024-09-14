# from typing import List, Optional, Dict

# # Book Class
# class Book:
#     def __init__(self, book_id: int, title: str, author: str, available: bool = True):
#         self.book_id = book_id
#         self.title = title
#         self.author = author
#         self.available = available

#     def display_info(self) -> None:
#         availability = 'Available' if self.available else 'Not Available'
#         print(f'ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Availability: {availability}')

# # User Class
# class User:
#     def __init__(self, user_id: int, name: str, email: str):
#         self.user_id = user_id
#         self.name = name
#         self.email = email

# # Librarian Class
# class Librarian(User):
#     def __init__(self, user_id: int, name: str, email: str):
#         super().__init__(user_id, name, email)

#     def add_book(self, library_manager, book: Book) -> None:
#         library_manager.add_book(book)

#     def update_book(self, library_manager, book_id: int, new_title: Optional[str], new_author: Optional[str], new_availability: Optional[bool]) -> None:
#         library_manager.update_book(book_id, new_title, new_author, new_availability)

#     def delete_book(self, library_manager, book_id: int) -> None:
#         library_manager.delete_book(book_id)

# # Member Class
# class Member(User):
#     def __init__(self, user_id: int, name: str, email: str):
#         super().__init__(user_id, name, email)

#     def borrow_book(self, library_manager, book_id: int) -> None:
#         library_manager.borrow_book(self.user_id, book_id)

#     def return_book(self, library_manager, book_id: int) -> None:
#         library_manager.return_book(self.user_id, book_id)

# # Library Manager Class
# class LibraryManager:
#     def __init__(self):
#         self.books: Dict[int, Book] = {}
#         self.users: Dict[int, User] = {}
#         self.load_books()
#         self.load_users()

#     def load_books(self) -> None:
#         try:
#             with open('books.txt', 'r') as file:
#                 for line in file:
#                     book_id, title, author, available = line.strip().split(',')
#                     self.books[int(book_id)] = Book(int(book_id), title, author, available == 'True')
#         except FileNotFoundError:
#             print("books.txt not found, starting with an empty library.")

#     def load_users(self) -> None:
#         try:
#             with open('users.txt', 'r') as file:
#                 for line in file:
#                     user_id, name, email, user_type = line.strip().split(',')
#                     if user_type == 'Librarian':
#                         self.users[int(user_id)] = Librarian(int(user_id), name, email)
#                     elif user_type == 'Member':
#                         self.users[int(user_id)] = Member(int(user_id), name, email)
#         except FileNotFoundError:
#             print("users.txt not found, starting with no users.")

#     def save_books(self) -> None:
#         with open('books.txt', 'w') as file:
#             for book in self.books.values():
#                 file.write(f'{book.book_id},{book.title},{book.author},{book.available}\n')

#     def save_users(self) -> None:
#         with open('users.txt', 'w') as file:
#             for user in self.users.values():
#                 user_type = 'Librarian' if isinstance(user, Librarian) else 'Member'
#                 file.write(f'{user.user_id},{user.name},{user.email},{user_type}\n')

#     def add_book(self, book: Book) -> None:
#         if book.book_id in self.books:
#             print("Book ID already exists.")
#             return
#         self.books[book.book_id] = book
#         self.save_books()
#         print(f'Book "{book.title}" added successfully.')

#     def update_book(self, book_id: int, new_title: Optional[str], new_author: Optional[str], new_availability: Optional[bool]) -> None:
#         if book_id not in self.books:
#             print("Book not found.")
#             return
#         book = self.books[book_id]
#         if new_title:
#             book.title = new_title
#         if new_author:
#             book.author = new_author
#         if new_availability is not None:
#             book.available = new_availability
#         self.save_books()
#         print(f'Book ID {book_id} updated successfully.')

#     def delete_book(self, book_id: int) -> None:
#         if book_id in self.books:
#             del self.books[book_id]
#             self.save_books()
#             print(f'Book ID {book_id} deleted successfully.')
#         else:
#             print("Book not found.")

#     def borrow_book(self, user_id: int, book_id: int) -> None:
#         if book_id not in self.books:
#             print("Book not found.")
#             return
#         book = self.books[book_id]
#         if not book.available:
#             print(f'The book "{book.title}" is currently not available.')
#             return
#         book.available = False
#         self.save_books()
#         print(f'User ID {user_id} borrowed "{book.title}".')

#     def return_book(self, user_id: int, book_id: int) -> None:
#         if book_id not in self.books:
#             print("Book not found.")
#             return
#         book = self.books[book_id]
#         if book.available:
#             print(f'The book "{book.title}" was not borrowed.')
#             return
#         book.available = True
#         self.save_books()
#         print(f'User ID {user_id} returned "{book.title}".')

# # Sample usage of the system

# # Initialize LibraryManager
# library_manager = LibraryManager()

# # Register users (Example)
# librarian = Librarian(1, "Alice", "alice@library.com")
# member = Member(2, "Bob", "bob@library.com")
# library_manager.users[librarian.user_id] = librarian
# library_manager.users[member.user_id] = member
# library_manager.save_users()

# # Librarian adds a book
# librarian.add_book(library_manager, Book(1, "The Great Gatsby", "F. Scott Fitzgerald"))

# # Member borrows the book
# member.borrow_book(library_manager, 1)

# # Member returns the book
# member.return_book(library_manager, 1)

# # Librarian deletes the book
# librarian.delete_book(library_manager, 1)

# # Display current books in the system
# for book in library_manager.books.values():
#     book.display_info()

from typing import List, Optional, ClassVar
import os


# Base Class: User
class User:
    def __init__(self, user_id: int, name: str, email: str):
        self._user_id = user_id
        self._name = name
        self._email = email

    def display_info(self):
        print(f"ID: {self._user_id}, Name: {self._name}, Email: {self._email}")


# Derived Class: Librarian
class Librarian(User):
    def __init__(self, user_id: int, name: str, email: str):
        super().__init__(user_id, name, email)

    def add_book(self, library_manager, book_id: int, title: str, author: str):
        library_manager.add_book(Book(book_id, title, author, True))

    def update_book(self, library_manager, book_id: int, title: Optional[str] = None, author: Optional[str] = None):
        library_manager.update_book(book_id, title, author)

    def delete_book(self, library_manager, book_id: int):
        library_manager.delete_book(book_id)


# Derived Class: Member
class Member(User):
    def __init__(self, user_id: int, name: str, email: str):
        super().__init__(user_id, name, email)

    def borrow_book(self, library_manager, book_id: int):
        library_manager.borrow_book(self._user_id, book_id)

    def return_book(self, library_manager, book_id: int):
        library_manager.return_book(self._user_id, book_id)


# Class: Book
class Book:
    def __init__(self, book_id: int, title: str, author: str, available: bool = True):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._available = available

    def display_info(self):
        availability = "Available" if self._available else "Not Available"
        print(f"ID: {self._book_id}, Title: {self._title}, Author: {self._author}, Status: {availability}")


# Class: LibraryManager
class LibraryManager:
    books_file: ClassVar[str] = "books.txt"
    users_file: ClassVar[str] = "users.txt"

    def __init__(self):
        self.books = []
        self.users = []
        self.load_books()
        self.load_users()

    def load_books(self):
        try:
            if os.path.exists(self.books_file):
                with open(self.books_file, "r") as f:
                    for line in f:
                        book_id, title, author, available = line.strip().split(',')
                        self.books.append(Book(int(book_id), title, author, available == 'True'))
        except Exception as e:
            print(f"Error loading books: {e}")

    def save_books(self):
        try:
            with open(self.books_file, "w") as f:
                for book in self.books:
                    f.write(f"{book._book_id},{book._title},{book._author},{book._available}\n")
        except Exception as e:
            print(f"Error saving books: {e}")

    def load_users(self):
        try:
            if os.path.exists(self.users_file):
                with open(self.users_file, "r") as f:
                    for line in f:
                        user_id, name, email = line.strip().split(',')
                        self.users.append(User(int(user_id), name, email))
        except Exception as e:
            print(f"Error loading users: {e}")

    def save_users(self):
        try:
            with open(self.users_file, "w") as f:
                for user in self.users:
                    f.write(f"{user._user_id},{user._name},{user._email}\n")
        except Exception as e:
            print(f"Error saving users: {e}")

    def add_book(self, book: Book):
        self.books.append(book)
        self.save_books()

    def update_book(self, book_id: int, title: Optional[str] = None, author: Optional[str] = None):
        for book in self.books:
            if book._book_id == book_id:
                if title:
                    book._title = title
                if author:
                    book._author = author
                self.save_books()
                return
        print(f"Book with ID {book_id} not found.")

    def delete_book(self, book_id: int):
        self.books = [book for book in self.books if book._book_id != book_id]
        self.save_books()

    def borrow_book(self, user_id: int, book_id: int):
        for book in self.books:
            if book._book_id == book_id:
                if book._available:
                    book._available = False
                    self.save_books()
                    print(f"Book {book._title} has been borrowed by user {user_id}")
                else:
                    print(f"Book {book._title} is not available.")
                return
        print(f"Book with ID {book_id} not found.")

    def return_book(self, user_id: int, book_id: int):
        for book in self.books:
            if book._book_id == book_id:
                book._available = True
                self.save_books()
                print(f"Book {book._title} has been returned by user {user_id}")
                return
        print(f"Book with ID {book_id} not found.")

    def list_books(self):
        for book in self.books:
            book.display_info()


# Testing the Implementation
if __name__ == "__main__":
    # Instantiate the library manager
    library_manager = LibraryManager()

    # Create a librarian
    librarian = Librarian(1, "John Doe", "john@example.com")

    # Librarian adding books
    librarian.add_book(library_manager, 101, "The Great Gatsby", "F. Scott Fitzgerald")
    librarian.add_book(library_manager, 102, "1984", "George Orwell")

    # List all books
    print("Listing all books:")
    library_manager.list_books()

    # Create a member
    member = Member(2, "Alice Smith", "alice@example.com")

    # Member borrows a book
    member.borrow_book(library_manager, 101)

    # List all books after borrowing
    print("\nListing all books after borrowing:")
    library_manager.list_books()

    # Member returns a book
    member.return_book(library_manager, 101)

    # List all books after returning
    print("\nListing all books after returning:")
    library_manager.list_books()
