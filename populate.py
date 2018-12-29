'''
Program: Populate 1.0
Purpose: Input for testing of TomeRater 1.0 program
Last Updated: 12/28/18
Creator: Kyle Harper
Contact: Github- KyHarper
'''

from TomeRater import *

Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678, 5.50)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345, 6.50)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452, 10.50)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938, 12.35)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010, 8.95)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000, 7.65)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)

#Uncomment these to test your functions:
Tome_Rater.print_catalog()
Tome_Rater.print_users()

print(Tome_Rater.most_positive_user())
print(Tome_Rater.highest_rated_book())
print(Tome_Rater.get_most_read_book())
print(Tome_Rater.get_worth_of_user("alan@turing.com"))
print(Tome_Rater.get_n_most_expensive_books(5))