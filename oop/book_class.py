#!/bin/bash
# book_class.py

class Book:
    def __init__(self, title: str, author: str, year: int):
        """Constructor to initialize a Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints a message when a book is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Returns a string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Returns a string that would recreate the Book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

# Example usage:
if __name__ == "__main__":
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    print(str(book))  # Output: 'The Great Gatsby' by F. Scott Fitzgerald, published in 1925
    print(repr(book))  # Output: Book('The Great Gatsby', 'F. Scott Fitzgerald', 1925)

