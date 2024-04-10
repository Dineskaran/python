import random
# case-sensitive
a = 5
A = "Srilanka"

print(a)
print(A)
print("------------------------------------")
# Rules
mynum = [1, 2, 3]   # starting should not be a num, no spaces, no "-"
print(mynum)
print("------------------------------------")
# multi word variable techniques:

# camel case
iLoveSrilanka = [1, 2, 3]
print(iLoveSrilanka)
# pascal case
ILoveSriLanka = [1, 2, 3]
print(ILoveSriLanka)

# snake case
i_Love_Srilanka = [1, 2, 3]
print(i_Love_Srilanka)
x = 10

"""# Operators# Arithmetic- +,-,/,%,**# relational - <,>,==,!=# logical- and or not# Membership operator - in, not in"""

print("------------------------------------")
a = 3    # (/,%)
b = 4
print("the answer is :", a**b)

print("------------------------------------")
a = 100   # logical
b = 200
if a == b:
  print("correct")
else:
  print("Not correct")
print("------------------------------------")

xx = 5
print(3 < xx < 10)
print(xx > 3 or xx < 10)

print("------------------------------------")

# format strings
name = "Joy"
age = 20

sample = f"Hello, my name is {name} and I'm {age} years old."
print(sample)

print("------------------------------------")
# range

sample = range(10)
for i in sample:
  print(i)

print("------------------------------------")

# range
def multiplication_table(n):
  for j in range(1, 16):
    print(f"{n} * {j} = {n * j}")
multiplication_table(10)

print("------------------------------------")


# random

# import random
print(random.randrange(1, 100))

print("------------------------------------")

# python casting - int,str,float

x = int(2.8)
y = int("3")
z = float(10)

print(x)
print(y)
print(z)

print("------------------------------------")

# Membership operator

txt = "I love srilanka"
print("USA" in txt)

# False

txt = "I love srilanka"
if "US" in txt:
    print("Yes, it's present")
else:
    print("Not present")

print("------------------------------------")

txt = "I love srilanka"
print("china" not in txt)

print("------------------------------------")

b = "Hello, srilanka!"

print(b[2:6])
print(b[3:])
print(b[:10])
print(b[-5:-2])  # negative indexing
print(b[::])
print(b.strip())  # removes whitespace at the beg and the end

print("------------------------------------")

b = "Hello, srilanka!"

print(b.strip())
print(b.replace("H", "J"))
print(len(b))
print(b.split("l"))

print("------------------------------------")

# escape characters
txt = "I love \"srilanka\" India and china"
print(txt)
print("------------------------------------")

txt = "I love \'srilanka\' India and china"
print(txt)
print("------------------------------------")

txt = "I love \'srilanka\' \nIndia and china"
print(txt)
print("------------------------------------")
"""
List -
mutable, ordered, []
append
pop
reverse
sort
slicing
for accesing list
"""
print("------------------------------------")


List = [100, 3, 5, 8, 7]
List.sort()     # ascending
print(List)

List.reverse()
print(List)

print("------------------------------------")
nested_tuple = ((1, 2), (3, 4))
print(nested_tuple)

print("------------------------------------")
tuple1 = (1, 2, 3)

result = tuple1 * 3
print(result)

print("------------------------------------")
# Set - Unordered collection of unique sumbols
# No duplicates, mutable also
# add.
# pop
# insert
# len

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
intersection_set = set1 & set2
difference_set = set2 - set1

print(union_set)
print(intersection_set)
print(difference_set)

print("------------------------------------")
list1 = [1, 2, 3, 2, 4, 4, 5]
result = set(list1)
print(result)

print("------------------------------------")

dicts = {"name": "joy", "age": 30, "city": "srilanka"}

dicts.update({"mark": 100})
print(dicts)

name1 = dicts["age"]
print(name1)

print("------------------------------------")

# Break statement
car = ["bmw", "audi", "polo"]
for i in car:
  print(i)
  if i == "audi":
    break
print("------------------------------------")


# continue
car = ["bmw", "audi", "polo"]
for i in car:
  if i == "audi":
    continue
  print(i)

print("--Functions - collection of statements, def----------------------------------")


# 1. With No arguments and No return

def add():
    a= 10
    b = 20
    sum = a + b
    print("calling the function:", sum)
add()

print("------------------------------------")


# 2. No argument and with return
def Multiplication():
    a = 10
    b = 20
    Multi = a * b
    return Multi

print("calling the function:", Multiplication())

print("------------------------------------")


# 3. With Argument and No return
def Multiplication(a, b):
    Multi = a * b
    print("calling the function:", Multi)


Multiplication(10, 20)

print("------------------------------------")

#4. With Argument and with return

def add(a,b):

  sum = a+b
  return sum
print("calling the function:",sum)
add(100,200)
print("=============!===========!==========!=======")
list = ['a', 'b', 'c', 'd']  # pass statement
for i in list:
    if (i == 'a'):
        pass
    else:
        print(i)
