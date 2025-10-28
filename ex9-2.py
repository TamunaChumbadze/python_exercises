"""
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
"""

class Restaurant:

    def __init__(self, restaurant, cuisine):
        self.restaurant_name = restaurant
        self.cuisine_type = cuisine

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

restaurant1 = Restaurant("Pizza Di Roma", "Italian")
restaurant2 = Restaurant("Sushi Room", "Japanese")
restaurant3 = Restaurant("Soule", "Korean")


restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()