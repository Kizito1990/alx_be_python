#!/bin/bash
class Book:
    def __init__(self, title:str, author: str):
        self.title = title
        self.author = author

    def get_info(self):
        print(f"Book: {self.title} by {self.author}")



class Ebook(Book)

    def __init__(self, file_size: int, title, author):
        super().__init__(title, author)
        self.file_size = file_size

    def get_info(self):
        print(f"Ebook: {self.title} by {self.author}, File Size: {self.file_size}")

class PrintBook(Book):
    def __init__(self, page_count: int, title, author):
        super().__init__(title, author)
        self.page_count = page_count


    def get_info(self):
        print(f"Ebook: {self.title} by {self.author}, Page Count: {self.page_count}")


class Library:
    def __init__(self, books):
        self.books = []


    def add_books(self, book):
        self.books.append(book)


    def list_book(self):
            for book in self.books:
                print(book.get_details())



