

# Types of Import Statements
# 1. Import From Module:
from math import sqrt, factorial
print(sqrt(16))
print(factorial(6))

# 2. Import All Names: *
from math import *
print(sqrt(16))
print(factorial(6))

# 3. Import With Alias: 
import math as m
print(m.pi)

# Types of Modules
# Python provides several kinds of modules. Each type plays a different role in application development.

# 1. Built-in Modules:
import random
print(random.randint(1, 5))

# 2. User-Defined Modules:
import  calc

print(calc.add(2, 3))
print(calc.subtract(5, 2))
print(calc.multiply(3, 4))
print(calc.divide(10, 2))

# 3. External (Third-Party) Modules:
import requests
r = requests.get("https://example.com")
print(r.status_code)

# 4. Package Modules: 
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src import testFunction
print(testFunction.addFun(2, 3))

for p in sys.path:
    print(p)