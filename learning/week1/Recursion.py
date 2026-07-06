# Recursion
# Recursion is when a function calls itself.
# Recursion is a common mathematical and programming concept. It means that a function calls itself.
#  This has the benefit of meaning that you can loop through data to reach a result.

def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

countdown(5)

# Identifying base case and recursive case:
def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))

# Fibonacci Sequence
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))


# Calculate the sum of all elements in a list:
def sum_list(numbers):
  if len(numbers) == 0:
    return 0
  else:
    return numbers[0] + sum_list(numbers[1:])

my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))


# Find the maximum value in a list:
def find_max(numbers):
  if len(numbers) == 1:
    return numbers[0]
  else:
    max_of_rest = find_max(numbers[1:])
    return numbers[0] if numbers[0] > max_of_rest else max_of_rest

my_list = [3, 7, 2, 9, 1]
print(find_max(my_list))


# Recursion Depth Limit
print("Recursion depth limit:")
import sys
print(sys.getrecursionlimit())

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())