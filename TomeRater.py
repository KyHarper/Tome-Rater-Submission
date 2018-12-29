'''
Program: TomeRater 1.0
Purpose: Structure and orginization of a book reading and rating tool. Created for capstone submsisson of Codecademy Pro Intensive: Python
Last Updated: 12/28/18
Creator: Kyle Harper
Contact: Github- KyHarper
'''

class User():

    #Definition of key variables, methods for adjusting variables, and initialization methods
    def __init__(self, name, email):
        self.name = name
        #Note: Email is used in this system as a unique identifier for adding books
        self.email = email
        # Key/value pairs = book title/user rating
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, new_address):
        self.email = new_address
        print("Your email address has been updated to: {address}.").format(address=new_address)

    def __repr__(self):
        return "Username {name}, Email: {email} , Books Read: {books}".format(name=self.name, email=self.email, books=len(self.books))

    def __eq__(self, comp_user):
        return self.name == comp_user.name and self.email == comp_user.email

    #Methods for interaction
    def read_book(self, book, rating = None):
        self.books[book] = rating

    def get_average_rating(self):
        rating_total = 0
        num_books = 0
        for book in self.books.keys():
            if self.books[book] != None:
                num_books += 1
                rating_total += self.books[book]
        return rating_total / num_books

class Book():

    # Definition of key variables, methods for adjusting key variables, and initialization methods
    def __init__(self, title, isbn, price):
        self.title = title
        self.isbn = isbn
        self.ratings = []
        self.price = price

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def get_price(self):
        return self.price

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("The ISBN for this book has been updated to {isbn}".format(isbn=new_isbn))

    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating. Ratings must be a value from 0 to 4. Please try again")

    def __repr__(self):
        return "A book called {title}".format(title=self.title)

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __eq__(self, comp_book):
        return self.title == comp_book.title and self.isbn == comp_book.isbn

    #Methods for interaction
    def get_average_rating(self):
        if len(self.ratings) == 0:
            return None
        total = 0
        for value in self.ratings:
                total += value
        return value / len(self.ratings)


#Definitions for two subclasses of book, Fiction (referred to later in code as "novels") and NonFiction (referred to later in code as "manuals")
class Fiction(Book):
    def __init__(self, title, author, isbn, price):
        super().__init__(title, isbn, price)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} written by {author}".format(title=self.title, author=self.author)

class NonFiction(Book):
    def __init__(self, title, subject, level, isbn, price):
        super().__init__(title, isbn, price)
        self.subject = subject
        self.level = level

    def __repr__(self):
        return "{title}, a {level} manual on the topic of {subject}".format(title=self.title, level=self.level, subject=self.subject)

class TomeRater():
    #Definition of key variables, methods for adjusting key variables, and initialization methods
    def __init__(self):
        #Key/value pairs = email / name of user
        self.users = {}
        #Key/value pairs = book title/number of users who have read
        self.books = {}

    #Methods for interaction
    def create_book(self, title, isbn, price):
        return Book(title, isbn, price)

    def create_novel(self, title, author, isbn, price):
        return Fiction(title, author, isbn, price)

    def create_non_fiction(self, title, subject, level, isbn, price):
        return NonFiction(title, subject, level, isbn, price)

    def add_book_to_user(self, book, email, rating=None):
        if email not in self.users:
            print("No user with email address {address} found!".format(address=email))
        else:
            self.users[email].read_book(book, rating)
            if rating != None:
                book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            if book not in self.books:
                self.books[book] = 1

    def add_user(self, name, email, user_books=None):
        if email in self.users:
            print("User could not be created. Email address already in use.")
        else:
            user = User(name, email)
            self.users[email] = user
            if user_books != None:
                for book in user_books:
                    self.add_book_to_user(book, email)

    #Methods useful for analysis of TomeRater data
    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.keys():
            print(user)

    def get_most_read_book(self):
        read_number = 0
        title = ""
        for key, value in self.books.items():
            if value > read_number:
                read_number = value
                title = key
        print("With {readers} reads in Tome Rater, the current most read book is:".format(readers=read_number))
        return title

    def highest_rated_book(self):
        best_rating = 0
        title = ""
        for key, value in self.books.items():
            rating = key.get_average_rating()
            if rating > best_rating:
                best_rating = rating
                title = key
        print("With an average rating of {rating}, our highest rated book is:".format(rating=best_rating))
        return title

    def most_positive_user(self):
        positive_user = None
        highest_rating = 0
        for user in self.users.values():
            avg_user_rating = user.get_average_rating()
            if avg_user_rating > highest_rating:
                positive_user = user
                highest_rating = avg_user_rating
        print("With an average rating of {average}, the most positve user is: ".format(average=highest_rating))
        return positive_user

    def get_n_most_expensive_books(self, n):
        most_expensive_books = []
        for book in self.books.keys():
            most_expensive_books.append((book.price, book))
        most_expensive_books.sort(reverse=True)
        if n > len(most_expensive_books):
            n = len(most_expensive_books)
        print("From most expensive to least expensive, the top {n} books are:".format(n=n))  
        return most_expensive_books[0:n]

    def get_worth_of_user(self, user_email):
        user_worth = 0
        user = self.users[user_email]
        for book in user.books:
            user_worth += book.price
        return "Total price of books owned by user {user}: ${value}".format(user=user_email, value = str(user_worth))
