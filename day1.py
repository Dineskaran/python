a = 8.4
b = "hello"
# hello
print(a)
print("=============================================")
if 10 > 2:
    print("Yes it's correct")
print("=============================================")

a = 8.4
b = "hello"
# hello
print(a)
print("=============================================")
a, b, c = "hello", "Hi", 8.9
print(c)
print("=============================================")

x = "Srilanka"
y = "India"
z = x +" "+ y
print(z)
print("=============================================")
x = "Srilanka"
def func():
  x = "India"
  print("I love" + x)
print("=============================================")

func()
print("I love" + x)
print("=============================================")
x = "hi"
def func():
  global x
  x = "hello"
func()
print("I love" + x)
print("=============================================")
a = ["hi", "hello", "welcome"]
print(type(a))
print("=============================================")
a = ("hi", "hello", "welcome")
print(type(a))
print("=============================================")
a = {"hi", "hello", "welcome"}
print(type(a))
print("=============================================")

x = 10
y = 2.6
z = 6+6j
a = float(x)
b = int(y)
c = complex(x)
print(a)
print(b)
print(c)
print("=============================================")
a = """hahshsh
shshjsh
shshsh"""
print(a)
print("=============================================")

a = "hello"
print(a[0])
print("=============================================")

b = "Welcome world"
print(b[-3])

print(len(b))

print(b.strip())

print(b.lower())
print(b.upper())

print(b.replace("W", "o"))
print("=============================================")

# Concatenation

a = "hi"
b = "welcome"
c = a + " " + b
print(c)
print("=============================================")

print(100<10)
print("=============================================")

a = 100
b = 200

if b > a:
    print("Yes correct")
else:
    print("Wrong")

print(bool("Hi"))

print("=============================================")

"""
Operators:
Arithmetic - =,-,/,*
Comparison - <,>.==
Loogical - and or not
Bitwise - and &
OR |
XOR ^
NOT -
"""



List =["india", "srilanka", "malaysia"]

for x in List:
  print(x)
  print(x)
print("=============================================")

list = ["india", "srilanka", "malaysia"]

if "india" in list:
    print("Yes")
else:
    print("No")
print(len(list))

list.append("singapore")
print(list)

list.insert(1, "asia")
print(list)

list.remove("malaysia")
print(list)

list.pop()
print(list)

print("=============================================")
list = ["india", "srilanka", "malaysia"]

list.pop()
print(list)

del list

print("=============================================")

list = ["india", "srilanka", "malaysia"]

list.clear()
print(list)
print("=============================================")

list1 = ["india", "srilanka", "malaysia"]
list2 = ["USA"]

list3 = list1 + list2
print(list3)

['india', 'srilanka', 'malaysia', 'USA']
"""append()
clear()
insert()
pop()
remove()
"""
print("=============================================")

x = ("india", "srilanka", "malaysia")
# y = list(x)
# y[1] = "USA"
# x = tuple(y)
# print(x)
print(len(x))
print("=============================================")

set = {"india", "srilanka", "malaysia"}
print(set)
print("=============================================")



set = {"india", "srilanka", "malaysia"}
set.add("USA")

print(set)

set.remove("india")
print(set)

set.clear()
print(set)

del set
print(set)
print("=============================================")


set1 = {"india", "srilanka", "malaysia"}
set2 = {"india", "srilanka", "malaysia", "USA"}

set3 = set1.union(set2)

print(set3)

print("=============================================")

set1 = {"india", "srilanka", "malaysia"}
set2 = {"india", "srilanka", "malaysia", "USA"}

set3 = set1.intersection(set2)

print(set3)
print("=============================================")


set1 = {"india", "srilanka", "malaysia"}
set2 = {"india", "srilanka", "malaysia", "USA"}

set1.update(set2)
print(set1)
print("===================update() intersection() union() add() clear()==========================")

dict = {
    "india": "chennai",
    "mumbai": "usa",
    "kerala": "kolkata"
}

print(type(dict))

print("=============================================")
