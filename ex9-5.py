"""
9-5. Login Attempts: Add an attribute called login_attempts to your User class
from Exercise 9-3. Write a method called increment_login_attempts()
that increments the value of login_attempts by 1. Write another method called
reset_login_attempts() that resets the value of login_attempts to 0.

Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
"""

class User: 
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"User's First Name: {self.first_name}")
        print(f"User's Last Name: {self.last_name}")
        print(f"User's Age: {self.age}")
        print(f"User's Email: {self.email}\n")
        print(f"Login Attempts: {self.login_attempts}")
    
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name} ! Welcome back!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts by 1."""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Reset the value of login_attempts to 0."""
        self.login_attempts = 0
    

user = User("Tamuna", "Tchumbadze", 33, "t.chumbadze@gmail.com")

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

user.describe_user()

user.reset_login_attempts()
user.describe_user()