from functools import reduce

numbers = [20, 65, 20, 70, 70, 80]

largest = reduce(lambda a, b: a if a > b else b, numbers)

print("Largest Number:", largest)