# #No: 1
# class Book:
#     def __init__(self, title, author, price, quantity):
#         self.title = title
#         self.author = author
#         self.price = price
#         self.quantity = quantity

#     def __str__(self):
#         return f"Booktitle: {self.title}; Author:{self.author}; Price:{self.price}; Quantity:{self.quantity}"
    
# class BookStore:
#     def __init__(self):
#         self.book_record = []

#     def add_book(self, book):
#         self.book_record.append(book)

#     def show_available_books(self):
#         for book in self.book_record:
#             print(f"=> {book.title} by {book.author}")

#     def sell_books(self, book, qnt):
#         for i in self.book_record:
#             if (book == i.title) and (qnt <= i.quantity):
#                 i.quantity -= qnt
#                 print(f"{qnt} copies of {i.title} by {i.author} sold.")
#                 return
#         else:
#             print(f"{book} is not available!")
#                 # break
    
#     def order_book(self):
#         print(f"Enter information of the book you want to order:")
#         title = input("Book title: ")
#         author = input("Book author: ")
#         price = int(input("Price: "))
#         quantity = int(input("Quantity: "))
#         for i in self.book_record:
#             if title == i.title:
#                 i.quantity += quantity
#                 break
#         else:
#             book = Book(title, author, price, quantity)
#             self.book_record.append(book)
    
#     # def __str__(self):  #str function can't return non-string type
#     #     return self.book_record

# BoiKoli = BookStore()

# book_1 = Book("Python Crash Course", "Eric", 400, 23)
# BoiKoli.add_book(book_1)
# book_2 = Book("Data Science From Scrach", "Grus", 350, 12)
# BoiKoli.add_book(book_2)
# book_3 = Book("Hands on ML", "Adrewes", 750, 7)
# BoiKoli.add_book(book_3)

# BoiKoli.show_available_books()
# print(book_1)
# BoiKoli.sell_books("Python Crash Course", 12)
# print(book_1)
# BoiKoli.order_book()
# BoiKoli.show_available_books()
# BoiKoli.order_book()
# BoiKoli.show_available_books()
# print(book_1)



#No: 2
class Hero:
    def __init__(self, name, special_power):
        self.name = name
        self.special_power = special_power
        self.attack_damage = 15
        self.total_health = 100



class Enemy:
    def __init__(self, colour):
        self.colour = colour
        self.attack_damage = 5
        self.total_health = 50

    