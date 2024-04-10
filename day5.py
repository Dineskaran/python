# sample class & object
class Book:
    def __init__(self, referenceno, title, author, price):
        self.referenceno = referenceno
        self.title = title
        self.author = author
        self.price = price

    def __repr__(self):  # special method
        return f"Book: {self.referenceno},title: {self.title}, Author:{self.author}, Price: {self.price} "


book1 = Book(121, "titanic", "Author1", 100)
book2 = Book(101, "titanic", "Author1", 200)
book3 = Book(121, "titanic", "Author1", 300)  # Instantiate method

print(book1)
print(book2)
print(book3)
print("-----------------------------------------------------------------------------------------------------------")


# polymorphism - on various classes, one method it occurs in various forms

class Dog:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} runs!")


class Fish:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} swims!")


class Bird:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} fly!")


dog1 = Dog("Jack")
fish1 = Fish("abc")
bird1 = Bird("cbv")

for i in (dog1, fish1, bird1):
    i.move()

print("-----------------=-----------------------------=----------------------=")


# Inheritance over polymorphism

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

        def move(self):
            print("Move")


class Car(Vehicle):
    @staticmethod
    def move():
        print("Run")  # pass


class Flight(Vehicle):
    @staticmethod
    def move():
        print("Fly")




class Boat(Vehicle):
    def move(self):
        print("swim")


car1 = Car("Audi", "A4")
flight1 = Flight("Indigo", "A320")
boat1 = Boat("Titanic", "123")

for i in (car1, flight1, boat1):
    print(i.brand)
    print(i.model)
    i.move()
    print("_+__________________+______________________+_____________+________________+_____________________+")


# Encapsulation - private attribute cannot be accesessed at outside.

class Product:
    def __init__(self, name, price):
        self.name = name  # public attribut
        self._price = price  # encapsulated attribue / private

    def get_price(self):
        return self._price  # getter method to access the encapsulated attribute

    def set_price(self, price):
        if price >= 0:
            self._price = price
        else:
            print("price cannot be negative")  # to modify the private attribute


product = Product("Samsung", 500)  # Instantiate

print("product Name:", product.name)  # public attribute

print("Product price:", product.get_price())  # private attribute

product.set_price(-600)
print("Updated Price:", product.get_price())
print("=====================================================================================================")

# Bookstore

class Book:
  def __init__(self, title, quantity, author, price):
    self.title = title
    self.quantity = quantity
    self.author = author
    self.__price = price #private attribute
    self.__discount = None


  def set_discount(self, discount):
    self.__discount = discount

  def get_price(self):
    if self.__discount:
      return self.__price * (1-self.__discount)  #1-0.2(20% discount)-->80% after discounted price
    else:
      return self.__price

  def __str__(self):
    return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, price: {self.get_price()} "

book1 = Book("abc", 20, "James", 100)

single_book = Book("abc", 1, "James", 200)
bulk_book = Book("cvbg", 20, "Jack", 200)
bulk_book.set_discount(0.20)

# print(single_book.get_price)
# print(bulk_book.get_price)
print(single_book)
print(bulk_book)

print("================ =========== ================ ================== ========= ===========  ========= ")

