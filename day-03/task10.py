product = ("mobile", 70000, 2)

print("Original Product:", product)

# Trying to change the price
try:
    product[1] = 55000

except TypeError as e:
    print("Error:", e)

# Correct way: Create a new tuple
updated_product = (product[0], 55000, product[2])

print("Updated Product:", updated_product)