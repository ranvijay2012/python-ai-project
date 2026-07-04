# A variable is only available from inside the region it is created. This is called scope.

# Local Scope

def myfunc():
  x = 300
  print(x)

myfunc()

# Function Inside Function
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


# Global Scope
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

# Naming Variables
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

# Global Keyword
def myfunc():
  global x
  x = 300

myfunc()

print(x)


x = 300
def myfunc():
  global x
  x = 200

myfunc()

print(x)

# Nonlocal Keyword
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

# The LEGB Rule
# Python follows the LEGB rule when looking up variable names, and searches for them in this order:

# Local - Inside the current function
# Enclosing - Inside enclosing functions (from inner to outer)
# Global - At the top level of the module
# Built-in - In Python's built-in namespace

x = "global"
def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)