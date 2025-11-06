"""
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.

Create several instances representing different users, and call both meth-
ods for each user.
"""

class User: 
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
    
    def describe_user(self):
        print(f"User's First Name: {self.first_name}")
        print(f"User's Last Name: {self.last_name}")
        print(f"User's Age: {self.age}")
        print(f"User's Email: {self.email}\n")
    
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name} ! Welcome back!")

user1 = User("Tamuna", "Tchumbadze", 33, "t.chumbadze@gmail.com")
user2 = User("Luka", "Beridze", 30, "luka@gmail.com")
user3 = User("Nino", "Kapanadze", 28, "nino@gmail.com")

user1.describe_user()
user1.greet_user()
print()

user2.describe_user()
user2.greet_user()
print()

user3.describe_user()
user3.greet_user()

        