temperatures = [0, 30, 40, 50, 60]

fahrenheit = list(map(lambda c: (c * 9/5) + 32, temperatures))

print("Celsius:", temperatures)
print("Fahrenheit:", fahrenheit)