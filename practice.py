# --- TASK 1: Input and Greeting ---
# logic: Uses the input() function to capture user keystrokes.
# f-strings (f"") are the modern way to format strings in Python.

name = input("Enter your name: ")
print(f"Hello, {name}!")

print("-" * 20) # Just a separator line

# --- TASK 2: Loops and Conditionals ---
# logic: The modulo operator (%) returns the remainder. 
# If a number divided by 2 has a remainder of 0, it is even.

numbers = [1, 5, 8, 12, 17, 20, 23, 42]

print("Even numbers from the list:")
for num in numbers:
    if num % 2 == 0:
        print(num)

print("-" * 20)

# --- TASK 3: Classes (OOP) ---
# logic: This is the Blueprint.
# __init__ is the constructor (runs automatically when you create a new Car).
# self refers to the specific instance of the car being created.

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def drive(self):
        print(f"The {self.color} {self.brand} is vrooming down the street!")

# Creating 'instances' of the Class (Actual objects)
my_car = Car("Tesla", "Red")
your_car = Car("Toyota", "Blue")

# Calling the method
my_car.drive()   # Output: The Red Tesla is vrooming down the street!
your_car.drive() # Output: The Blue Toyota is vrooming down the street!
