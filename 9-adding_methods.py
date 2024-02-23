# Modify the Book class from Exercise 1 and add the describe_book method

# Call the describe_book method here
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe_book(self):
        print(f"Title: {self.title} Author: {self.author}")


book = Book("Python Basics", "John Doe")
book.describe_book()
