class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

class Library():

    def __init__(self):
        self.available_books = []

    def add_book(self, book):
        if isinstance(book, Book):  # Check if the parameter is a Book object
            self.available_books.append([book.title, book.author, book.is_checked_out])

    def list_available_books(self):
        for book in self.available_books:
            if book[2] != True:
                print(f"{book[0]} by {book[1]}")

    def check_out_book(self, title):
        for book in self.available_books:
            if title == book[0] and book[2] == False:
                book[2] = True

    def return_book(self, title):
        for book in self.available_books:
            if book[2] == True:
                book[2] = False