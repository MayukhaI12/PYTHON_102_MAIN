class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Book_Collection:
    def __init__(self):
        self.books_list = []

    def add_book(self, book):
        self.books_list.append(book)

    def remove_book(self, book):
        self.books_list.remove(book)

    def __iter__(self):
        return iter(self.books_list)

    def __next__(self):
        # Check if there are more books in the list
        if not self.books_list:
            raise StopIteration
        return self.books_list.pop(0)  # Return and remove the first book

# Create 5 books
book1 = Book("The Lord of the Rings", "J.R.R. Tolkien")
book2 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams")
book3 = Book("Pride and Prejudice", "Jane Austen")
book4 = Book("To Kill a Mockingbird", "Harper Lee")
book5 = Book("The Great Gatsby", "F. Scott Fitzgerald")

# Add the books to the Book_Collection
book_collection = Book_Collection()
book_collection.add_book(book1)
book_collection.add_book(book2)
book_collection.add_book(book3)
book_collection.add_book(book4)
book_collection.add_book(book5)

# Iterate over the books in the Book_Collection using a for loop
for book in book_collection:
    print(f"Title: {book.title}, Author: {book.author}")