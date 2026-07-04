# Lambda Functions
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# lambda arguments : expression

x = lambda a : a + 10
print(x(5))
print((lambda a : a + 10)(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))

mytripler = myfunc(3)
print(mytripler(11))

numbers = [1, 2, 3, 4, 5]
a = map(lambda x: x + 2, numbers)
for num in a:
    print(num)

print(list(a))

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)