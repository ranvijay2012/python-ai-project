# Generators are functions that can pause and resume their execution.
# When a generator function is called, it returns a generator object,
#  which is an iterator.
# The code inside the function is not executed yet, it is only compiled. 
# The function only executes when you iterate over the generator.

# def my_generator():
#   yield 1
#   yield 2
#   yield 3

# print("Generator output:"+ str(list(my_generator())))
# for value in my_generator():
#   print(value)

# Generators allow you to iterate over data without storing the entire dataset in memory.
# Instead of using return, generators use the yield keyword.

# def count_up_to(n):
#   count = 1
#   while count <= n:
#     yield count
#     count += 1

# for num in count_up_to(5):
#   print(num)

#   Unlike return, which terminates the function, yield pauses it and can be called multiple times.
# Generators are memory-efficient because they generate values on-the-fly instead of storing everything in memory.
# For large datasets, generators save memory:
# def large_sequence(n):
#   for i in range(n):
#     yield i

# # This doesn't create a million numbers in memory
# gen = large_sequence(10)
# print(gen)

# for num in gen:
#     print(num)

# print(next(gen))
# print(next(gen))
# print(next(gen))

def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))