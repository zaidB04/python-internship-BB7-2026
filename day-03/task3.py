numbers = [10, 20, 30, 10, 40, 20, 50, 30, 60, 10, 70, 80, 50, 90, 20]

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("Original List:", numbers)
print("Unique List:", unique_numbers)