
# Arguments
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the actual value that is sent to the function when it is called.

def my_function(name):          #here name is a parameter
    print(f"Hello {name} Welcome to the function!")

my_function("John")         #here John is an argument


# Number of Arguments
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", "Refsnes")


# Default Parameter Values
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")


# Keyword Arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

# Positional Arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")


# Mixing Positional and Keyword Arguments
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)


# Passing Different Data Types
# Sending a list as an argument:
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

# Sending a dictionary as an argument:
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)


# Return Values
def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)

# Returning Different Data Types
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(my_function()[0])
print(fruits[1])
print(fruits[2])


# A function that returns a tuple:
def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)
print(my_function()[0])
print(my_function()[1])

# Positional-Only Arguments
# You can specify that a function can have ONLY positional arguments.
# To specify positional-only arguments, add , / after the arguments:
def my_function(name, /):
  print("Hello", name)

# my_function({fname : "Emil", lname : "Linus"})  #error: got some positional-only arguments passed as keyword arguments: 'name'
my_function(("jhon", "doe")) 
my_function(["jhon", "doe"])
my_function("Emil")
# my_function(name = "Emil")      #error: got some positional-only arguments passed as keyword arguments: 'name'


# Keyword-Only Arguments
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")
# my_function({fname : "Emil", lname : "Linus"}) #error: got some positional-only arguments passed as keyword arguments: 'name'
# my_function("Emil")           #error: got some positional-only arguments passed as keyword arguments: 'name'
# my_function(("jhon", "doe"))  #error: got some positional-only arguments passed as keyword arguments: 'name'
# my_function(["jhon", "doe"])  #error: got some positional-only arguments passed as keyword arguments: 'name'


# Combining Positional-Only and Keyword-Only
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
# print( my_function(5, 10,  15, d = 20))   #error: got some positional-only arguments passed as keyword arguments: 'c'
# print( my_function(5, b = 10, c = 15, d = 20))    #error: got some positional-only arguments passed as keyword arguments: 'b'