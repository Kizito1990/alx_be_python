#!/bin/bash
class Book:
    def __init__(self,title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

class Ebook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size


    def __str__(self):
        return f"Ebook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        retyurn f"PrintBook: {self.title} by {self.author}, Page count: {self.page_count}"

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
