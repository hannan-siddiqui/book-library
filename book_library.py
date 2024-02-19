class Book:
    def _init_(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.status = 'available'

    def borrow_book(self):
        if self.status == 'available':
            self.status = 'borrowed'
            return True
        return False

    def return_book(self):
        self.status = 'available'

class Library:
    def _init_(self):
        self.books = {}

    def add_book(self, new_book):
        self.books[new_book.isbn] = new_book

    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]

    def borrow_book(self, isbn):
        if isbn in self.books and self.books[isbn].borrow_book():
            return True
        return False

    def return_book(self, isbn):
        if isbn in self.books:
            self.books[isbn].return_book()

    def search_books(self, title=None, author=None, publication_year=None):
        results = []
        for book in self.books.values():
            if title and title.lower() not in book.title.lower():
                continue
            if author and author.lower() not in book.author.lower():
                continue
            if publication_year and publication_year != book.publication_year:
                continue
            results.append(book)
        return results

