import pytest
from book_library import Book, Library

def test_book_creation():
    book = Book("Test Book", "Test Author", "1234567890", "2022")
    assert book.title == "Test Book"
    assert book.author == "Test Author"
    assert book.isbn == "1234567890"
    assert book.publication_year == "2022"
    assert book.status == "available"

def test_add_book_to_library():
    library = Library()
    book = Book("Test Book", "Test Author", "1234567890", "2022")
    library.add_book(book)
    assert library.books.get("1234567890") is not None

def test_remove_book_from_library():
    library = Library()
    book = Book("Test Book", "Test Author", "1234567890", "2022")
    library.add_book(book)
    library.remove_book("1234567890")
    assert library.books.get("1234567890") is None

def test_borrow_book():
    library = Library()
    book = Book("Test Book", "Test Author", "1234567890", "2022")
    library.add_book(book)
    assert library.borrow_book("1234567890") is True
    assert book.status == "borrowed"

def test_return_book():
    library = Library()
    book = Book("Test Book", "Test Author", "1234567890", "2022")
    library.add_book(book)
    library.borrow_book("1234567890")
    library.return_book("1234567890")
    assert book.status == "available"

def test_search_books():
    library = Library()
    book1 = Book("Test Book One", "Test Author", "1234567890", "2022")
    book2 = Book("Test Book Two", "Another Author", "0987654321", "2021")
    library.add_book(book1)
    library.add_book(book2)
    results = library.search_books(title="Test Book One")
    assert len(results) == 1
    assert results[0].isbn == "1234567890"
