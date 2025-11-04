
"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class Add an
attribute called flavors that stores a list of ice cream flavors. Write a
method that displays these flavors. Create an instance of IceCreamStand,
and call this method.
"""

class Restaurant:

    def __init__(self, restaurant, cuisine):
        self.restaurant_name = restaurant
        self.cuisine_type = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")
        print(f"Number served: {self.number_served}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        """Set the number of customers that have been served."""
        if number >= self.number_served:
            self.number_served = number
        else:
            print("You can't reduce the number served!")
    
    def increment_number_served(self, number):
        """Increment the number of custumers served"""
        if number > 0:
            self.number_served += number
        else:
            print("You must add a positive number!")

class IceCreamStand(Restaurant):
    """A class representing an ice cream stand, a specific kind of restaurant."""
    def __init__(self, restaurant, cuisine):
        super().__init__(restaurant, cuisine)
        self.flavors = ["chocolate", "vanilla", "Strawberry"]
    def disflay_flavors(self):
        print("Available ice cream flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

my_stand = IceCreamStand("Sweet Ice", "Dessert")
my_stand.disflay_flavors()