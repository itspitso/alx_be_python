class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, filesize):
        super().__init__(title, author)
        self.filesize = filesize

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.filesize}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    books = []
    def __init__(self):
        pass

    def add_book(self, book):
        Library.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)