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

    def add_book(self, book):
        self.book_record.append(book)

    def show_available_books(self):
        for book in self.book_record:
            print(f"=> {book.title} by {book.author}")

    def sell_books(self, book):
        for i in self.book_record:
            if book == i.titel:
                i.quantity -= 1
        
        


    def __str__(self):  #str function can't return non-string type
        return self.book_record

record = BookStore()
print(record)
