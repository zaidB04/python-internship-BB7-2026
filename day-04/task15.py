def safe_division(a, b):

    try:
        result = a / b
        return result

    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

    except TypeError:
        print("Error: Please enter valid numeric values!")


print(safe_division(20, 2))
print(safe_division(35, 0))
print(safe_division(10, "hyyy"))