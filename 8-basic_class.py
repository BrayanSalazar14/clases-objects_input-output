# Write your class definition here

# Create an instance of Book here
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


book = Book("Python Basics", "John Doe")
print(book.title)
print(book.author)
