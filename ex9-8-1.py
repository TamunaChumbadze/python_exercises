"""
9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
"""


class User:
    """Represent a simple user profile."""

    def __init__(
        self, first_name: str, last_name: str, username: str, email: str, location: str
    ):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0

class Privileges:
    """A class to represent privileges of an admin user."""
    def __init__(self, privileges=None):
        """Initialize the privileges attribute."""
        if privileges is None:
            self.privileges = []
        else:
            self.privileges = privileges
    
    def show_privileges(self):
        """Display the privileges."""
        if self.privileges:
            print("\nPrivileges:")
            for privilege in self.privileges:
                print(f"[*] {privilege}")
        else:
            print("\nThis admin has no privileges assigned.")


class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()

admin_user = Admin("Tamuna", "Tchumbadze", "tamuna33", "t.chumbadze@gmail.com", "Tbilisi")
admin_user.privileges.privileges = [
    "can add posts",
    "can delete posts",
    "can ban user",
    "can create advertisements"
]

admin_user.describe_user()
admin_user.privileges.show_privileges()