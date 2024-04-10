# Assigning a Function to a Variable

def multiply(a, b):
    return a * b

product = multiply  # assigning the function multiply to variable product
print(product(5, 6))  # calling the function using product

print("----------------------------")

# Passing a Function as Argument to another Function

def display(func):
    print("This is the display function")
    func()


def message():
    print("Welcome everyone!")
display(message)
print("-----------------------------")

# Defining a Function inside another Function (Nested Function)

def outer():
    def inner():  # defining nested function
        print("This is nested function")

    print("This is outer function")
    inner()  # calling nested function

outer()  # calling outer function
print("-------------------------------")
# Returning a Nested Function from its Parent Function
def outer():
    def inner():  # defining nested function
        print("Welcome everyone!")

    return inner  # returning nested function


message = outer()  # calling outer function
message()
print("-------------------------------")

# The function inner() is a nested function of the function outer().
def outer(x):
    def inner():
        print(x)

    return inner  # returning inner function

message = outer("Hey there!")
message()
print("--------------------------------")

# To understand decorators, let’s first look at the simplest following example of functions.
def normal():
    print("I am a normal function")

normal()
print("--------------------------------")
# Here we have a simple function named normal. Let’s make this function a little bit pretty.
def decorator_func(func):
    def inner():
        print("hi ")
        func()
        print("dines")

    return inner  # returning inner function

def normal():
    print("I am a normal function")

decorated_func = decorator_func(normal)
decorated_func()
print("--------------------------------")
def decorator_func(func):
    def inner():
        print("hi")
        func()
        print("Dosha")

    return inner  # returning inner function

def normal():
    print("I am a normal function")

normal = decorator_func(normal)
normal()
print("---------------------------------")
# For example, in the above program, we can replace the following piece of code
def normal():
    print("I am a normal function")

normal = decorator_func(normal)
print("--------------------------------")
@decorator_func
def normal():
    print("I am a normal function")
print("--------------------------------")
def decorator_func(func):
    def inner():
        print("Hi")
        func()
        print("Chayan")

    return inner  # returning inner function

@decorator_func
def normal():
    print("I am a normal function")

normal()
print("--------------------------------")
def decorator_lowercase(func):
    def to_lower():
        text = func()
        lowercase_text = text.lower()
        return lowercase_text

    return to_lower  # returning inner function

@decorator_lowercase
def message():
    return "I Am a Normal Function"

print(message())
print("--------------------------------")
# Passing Parameterized Functions to Decorators
def divide(num1, num2):
    return num1/num2
print("--------------------------------")
# To handle the case of 0 as the second parameter, let’s wrap the function in a decorator as shown below.
def decorator_division(func):
    def division(a, b):
        if b == 0:
            return "Can't divide!"
        else:
            return a/b

    return division  # returning inner function

@decorator_division
def divide(num1, num2):
    return num1/num2

print(divide(10, 2))
print("---------------------------------")
# Python Chaining Decorators
def decorator_star(func):
    def inner():
        print("It's")
        func()
        print("Me")

    return inner  # returning inner function

def decorator_hash(func):
    def inner():
        print("Hello")
        func()
        print("wold")

    return inner  # returning inner function

@decorator_star
@decorator_hash
def normal():
    print("I am a normal function")

normal()
print("-----------------------------------")

"""
I am a normal function
We applied two decorators decorator_star and decorator_hash to the normal() function. Note that the order in which we apply the decorators to the function matters.
"""
# In the above example, the following code
@decorator_star
@decorator_hash
def normal():
    print("I am a normal function")
print("-----------------------------------")


def decorator_star(func):
    def inner():
        print("Dark")
        func()
        print("Devil")

    return inner  # returning inner function


def decorator_hash(func):
    def inner():
        print("Kali")
        func()
        print("Cyber")

    return inner  # returning inner function


@decorator_hash
@decorator_star
def normal():
    print("I am a normal function")
normal()


