def convert_to_frozenset(my_list):

    return frozenset(my_list)


numbers = [20, 30, 40, 50, 30, 20]

result = convert_to_frozenset(numbers)

print("Original List:", numbers)

print("Frozenset:", result)

print("Type:", type(result))