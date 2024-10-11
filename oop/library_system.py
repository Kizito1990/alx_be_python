#!/bin/bash
# library_system.py

class Book:
    def __init__(self, title: str, author: str):
        """Constructor to initialize the book's title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation of a book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """Constructor to initialize the title, author, and file size of the ebook."""
        super().__init__(title, author)
        self.file_size = file_size  # in megabytes

    def __str__(self):
        """String representation of an ebook."""
        return f"Ebook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """Constructor to initialize the title, author, and page count of the print book."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """String representation of a print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Constructor to initialize the library with an empty list of books."""
        self.books = []

    def add_book(self, book: Book):
        """Adds a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """Prints details of each book in the library."""
        if not self.books:
            print("The library has no books.")
        else:
            for book in self.books:
                print(book)

