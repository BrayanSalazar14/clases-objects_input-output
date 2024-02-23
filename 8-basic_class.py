# Write your class definition here

# Create an instance of Book here
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe_book(self):
        print(f"Title: {self.title} Author: {self.author}")


title = input("Ingresa el titulo: ")
author = input("Ingresa el author: ")
book = Book(title, author)
book.describe_book()
