class Dog:
    """A simple attempt to model a dog.""" #ამ ტექსტს დოგ სტრინგს ჩვენთვის ვწერთხოლმე, პითონს არ ეხება, ჩვენი ჩანაწერივითაა

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over!")

my_dog = Dog("Will", 6)
your_dog = Dog("Lucy", 3)

# print(type(my_dog))

print(f"My dog's name is {my_dog}")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

print(f"/nYour dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()

