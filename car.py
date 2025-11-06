class Car:
    """A simple attempt to represent a car.""" 
    # ინიტს ქოლი(გამოძახება) არ სჭირდება. საკმარისი კლასი დავწეროთ და ეს თვითნვე გულისხმობს გამოძახებას. კლასს აქვს ატრიბუტი და მეთოდი
    # არ არის აუცილებელი ატრიბუტს დავუწეროთ მნიშვნელობა ინიტში, შეგვიძლია კლასის შიგნითაც დავწეროთ ატრიბუტი და მნიშვნელობა
    # init არის კონსტრუქტორი რომელიც ავტომატურად იძახება როცა კლასის ახალი ობიექტი იქმნება 
    # Self არის ობიექტის რეფერენცია რომელიც საშუალებას გვაძლევს მივწვდეთ კლასის ატრიბუტებს და მეთოდებს. წარმოადგენს კონკრეტულ ობიექტს რომელიც კლასის საფუძველზე იქმნება.
    def __init__(self, make, model, year):
        """Initialize attributes ro describing a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # ატრიბუტი რომელიც ინახავს კილომეტრაჟს, დეფოლტად შეიძლება დავწეროთ

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage): # განაახლება, გადააწერს ახალ მნიშვნელობას
        """
        Set the odomiter reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back on odometer!")
    
    def increment_odometer(self, miles): # ყოველ ქოლზე ამატებს მითითებულ მნიშვნელობას
        """Add the given amount to the odometer reading."""
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You are not allowed decrement!")

    # def fill_gas_tank(self):
    #     print(f"({self.make} gas tank is full.)")

# # print(end="") # ეს არის იმისთვის რომ შემდეგი პრინტი იგივე ხაზზე დაბეჭდოს 

# my_new_car = Car("audi", "a4", 2025)
# print(my_new_car.get_descriptive_name())

# # my_new_car.read_odometer()

# # my_new_car.odometer_reading = 23
# # my_new_car.read_odometer()

# my_new_car.update_odometer(23)
# my_new_car.update_odometer(13)
# my_new_car.read_odometer()

# my_used_car = Car("subaru", "outback", 2019)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(1000)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(-1000)
# my_used_car.read_odometer()


# გამეორება
# my_car = Car("audi", "a4", 2024)
# print(my_car.get_descriptive_name())
# my_car.read_odometer()  #დეფოლტი წავიკითხეთ

# my_car.odometer_reading = 23 # პირდაპირ ვცვლით მნიშვნელობას
# my_car.read_odometer()

# # my_car.update_odometer(24)
# # my_car.read_odometer()

# # my_car.update_odometer(10)
# # my_car.read_odometer()

# my_car.update_odometer(23_500)
# my_car.read_odometer()

# my_car.increment_odometer(100)
# my_car.read_odometer()

# my_car.increment_odometer(100)
# my_car.read_odometer()

# ახალი გაკვეთილი 
class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=40):
        """Initialize the batteru's attributes"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size} -kwh battery.")
    
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vechicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year) # super() ფუნქცია იძახებს მშობელ კლასს  შვილობილში და საშუალებას გვაძლევს მივწვდეთ მის მეთოდებს და ატრიბუტებს 
        self.battery = Battery() # ატრიბუტი რომელიც ეკუთვნის მხოლოდ electric car  კლასს
    


    # def fill_gas_tank(self):
    #     print("This car doesn't need a gas tank!")


my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

# my_leaf.describe_battery()


# my_bmw = Car("bmw", "i8", 2024)
# my_bmw.fill_gas_tank()
