# Task 1: Filter product prices using List Comprehension

# List of product prices
prices = [100, 200, 150, 300, 250, 120, 400, 180, 220, 280]

# Calculate average price
average = sum(prices) / len(prices)

# Create a new list using List Comprehension
above_average = [price for price in prices if price > average]

# Display results
print("Product Prices:", prices)
print("Average Price:", average)
print("Prices Above Average:", above_average)