class Book:
    def __init__(self, title, author, price, quantity):
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Booktitle: {self.title}; Author:{self.author}; Price:{self.price}; Quantity:{self.quantity}"
    
class BookStore:
    def __init__(self):
        self.book_record = []
        book_entry = int(input("Enter the amount of books you want to entry: "))
        for i in range(book_entry):
            book_title = input("Enter book title: ")
            book_author = input("Enter book author: ")
            book_price = input("Enter the price of the book: ")
            book_quantity = input("Enter book quantity: ")
            self.book_record.append(Book(book_title, book_author, book_price, book_quantity))

    def __str__(self):
        return self.book_record

record = BookStore()
print(record)
