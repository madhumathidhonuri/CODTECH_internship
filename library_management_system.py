from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        self.due_date = None
        
class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.borrowed_books = []
        self.fines = 0
        
class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.fine_per_day = 5
    
    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f'Book "{book.title}" by {book.author} added to the library.')
    
    def add_member(self, name, username, password):
        member = Member(name, username, password)
        self.members.append(member)
        print(f'Member {name} added to the library.')
    
    def authenticate_member(self, username, password):
        for member in self.members:
            if member.username == username and member.password == password:
                return member
        return None
    
    def display_books(self):
        print("Available books in the library:")
        for book in self.books:
            if not book.is_borrowed:
                print(f'{book.title} by {book.author}')
    
    def search_book_by_author(self, author):
        print(f"Search results for books by author: {author}")
        for book in self.books:
            if book.author.lower() == author.lower():
                status = "borrowed" if book.is_borrowed else "available"
                print(f'Book "{book.title}" by {book.author} is currently {status}.')
    
    def borrow_book(self, title, member):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                book.due_date = datetime.now() + timedelta(days=15)
                member.borrowed_books.append(book)
                print(f'{member.name} borrowed "{book.title}". Due date is {book.due_date.strftime("%Y-%m-%d")}.')
                return
        print(f'Sorry, the book "{title}" is either not available or already borrowed.')
    
    def return_book(self, title, member):
        for book in member.borrowed_books:
            if book.title == title:
                book.is_borrowed = False
                member.borrowed_books.remove(book)
                overdue_days = (datetime.now() - book.due_date).days
                if overdue_days > 0:
                    fine = overdue_days * self.fine_per_day
                    print(f'{member.name} returned "{book.title}". Overdue by {overdue_days} days. Fine: ${fine}')
                else:
                    print(f'{member.name} returned "{book.title}" on time.')
                return
        print(f'{member.name} did not borrow the book "{title}".')

# Testing the code
library = Library()
library.add_book("Python Programming", "John Doe")
library.add_book("Machine Learning", "Jane Smith")
library.add_member("Madhu", "madhu123", "12345")
library.add_member("Chinna", "chinna123", "password")

# Authenticate member
member = library.authenticate_member("madhu123", "12345")
if member:
    library.borrow_book("Python Programming", member)

library.display_books()

if member:
    library.return_book("Python Programming", member)

library.display_books()

library.search_book_by_author("Jane Smith")
