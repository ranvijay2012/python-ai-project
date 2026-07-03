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