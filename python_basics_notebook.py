# Jupyter Notebook: Python Basics (Syntax to Functions) - Detailed Explanations Including Dictionaries

# ------------------------
# 1. Basic Syntax and Comments
# ------------------------

# Single-line comment: Anything after # is ignored by Python
print("Hello, World!")  # Prints 'Hello, World!' to the console

# Multi-line comment: You can use triple quotes to write multiple lines of comments
'''
This is a multi-line comment.
It can span several lines.
Useful for explanations or temporarily disabling code.
'''

# ------------------------
# 2. Variables and Data Types
# ------------------------

# Variables are used to store data. Python automatically detects the type.

# Integer: whole numbers
x = 10
print(x, type(x))  # Outputs 10 <class 'int'>

# Float: decimal numbers
y = 3.14
print(y, type(y))  # Outputs 3.14 <class 'float'>

# String: sequence of characters
name = "Alice"
print(name, type(name))  # Outputs Alice <class 'str'>

# Boolean: True or False
flag = True
print(flag, type(flag))  # Outputs True <class 'bool'>

# List: ordered, changeable collection of elements
fruits = ["apple", "banana", "cherry"]
print(fruits, type(fruits))

# Tuple: ordered, immutable collection of elements
coordinates = (10, 20)
print(coordinates, type(coordinates))

# Dictionary: unordered collection of key-value pairs
student = {"name": "Bob", "age": 22, "track": "Math"}
print(student, type(student))  # Prints the dictionary and its type

# Access dictionary values by key
print(student['name'])  # Access value for key 'name'

# Add or update dictionary entries
student['grade'] = 'A'  # Add new key-value pair
student['age'] = 23      # Update existing key 'age'
print(student)

# Remove items from dictionary
del student['track']  # Remove the key 'track'
print(student)

# Loop through dictionary
for key, value in student.items():  # Iterate over key-value pairs
    print(f"{key}: {value}")

# Set: unordered collection of unique elements
unique_numbers = {1, 2, 3, 3}  # Duplicates are removed automatically
print(unique_numbers, type(unique_numbers))

# ------------------------
# 3. Operators
# ------------------------

# Arithmetic operators: +, -, *, /, %, ** (power), // (floor division)
print(5 + 3, 5 - 3, 5 * 3, 5 / 3, 5 % 3, 5 ** 2, 10 // 3)

# Comparison operators: >, <, ==, !=, >=, <=
print(5 > 3, 5 < 3, 5 == 5, 5 != 3)

# Logical operators: and, or, not
print(True and False, True or False, not True)

# Assignment operators: =, +=, -=, *=, /= etc.
a = 5
print(a)  # 5

a += 2  # equivalent to a = a + 2
print(a)  # 7

# ------------------------
# 4. Conditional Statements
# ------------------------

age = 20
# if statement: executes block if condition is True
# elif statement: checks another condition if previous if was False
# else: executes if all above conditions are False
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# ------------------------
# 5. Loops
# ------------------------

# For loop: used to iterate over a sequence (list, range, string, dictionary keys/values, etc.)
for i in range(5):  # Loop from 0 to 4
    print(f"Iteration {i}")

# While loop: continues as long as condition is True
count = 0
while count < 5:
    print(f"Count = {count}")
    count += 1  # Increment count to avoid infinite loop

# Break and continue
for i in range(5):
    if i == 3:
        continue  # Skip the rest of this loop iteration and continue to next
    if i == 4:
        break     # Exit the loop entirely
    print(i)

# Loop through dictionary
for key, value in student.items():
    print(f"{key} -> {value}")

# ------------------------
# 6. Functions
# ------------------------

# Functions are reusable blocks of code that perform a specific task

# Function with no parameters
def greet():
    print("Hello!")

greet()  # Call the function

# Function with parameters
def add(a, b):
    # 'a' and 'b' are inputs; the function returns their sum
    return a + b

result = add(5, 3)
print(f"Sum = {result}")

# Function with default parameter
def power(base, exp=2):
    # 'exp' defaults to 2 if not provided
    return base ** exp

print(power(4))      # Uses default exponent 2 → 4^2 = 16
print(power(2, 3))   # Overrides exponent → 2^3 = 8

# Function with variable number of arguments
def fruits_list(*args):
    # '*args' allows passing any number of positional arguments
    for fruit in args:
        print(fruit)

fruits_list("apple", "banana", "cherry")

# Function with keyword arguments
def student_info(**kwargs):
    # '**kwargs' allows passing any number of key-value pairs
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_info(name="Alice", age=21, track="Math")
