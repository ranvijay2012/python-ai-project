def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@changecase
def myfunction(a):
  return "Hello Sally " + a

@changecase
def otherfunction(a):
  return "I am speed! "  + a

print(otherfunction("john"))
print(myfunction("john"))

# Preserving Function Metadata
# Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.
# Normally, a function's name can be returned with the __name__ attribute:

def myfunction():
  return "Have a great day!"

print(myfunction.__name__)
print(myfunction.__doc__)

# But, when a function is decorated, the metadata of the original function is lost.
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

# To fix this, Python has a built-in function called functools.wraps that can be used to preserve the original function's name and docstring.
print("Using functools.wraps to preserve function metadata")
import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

# Multiple Decorators
print("Using multiple decorators")
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())