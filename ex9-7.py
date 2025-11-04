
"""
9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class. Add an attribute, privileges, that
stores a list of strings like "can add post", "can delete post",
"can ban user", and so on. Write a method called show_privileges() that
lists the administrator’s set of privileges. Create an instance of Admin,
and call your method.
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
    

class Admin(User):
    """A class representing on adminisstrator, a special kind of user."""
    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email)
        self.privileges = []

    def show_privileges(self):
        print("Admin Privileges:")
        for privilege in self.privileges:
            print(f" - {privilege}")

admin_user = Admin("Tamuna", "Chumbadze", 33, "t.chumbadze@gmail.com")
admin_user.privileges = [ 
    "can add posts", 
    "can delete posts", 
    "can ban user", 
    "can create advertisments"
    ]
admin_user.show_privileges()