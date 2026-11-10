class InvalidNumberError(Exception):
    pass


while True:

    try:
        number = int(input("Enter a number between 2 and 20: "))

        if number < 2 or number > 20:
            raise InvalidNumberError("Number must be between 1 and 10!")

        print("Valid Number:", number)
        break

    except ValueError:
        print("Error: Please enter a numeric value!")

    except InvalidNumberError as e:
        print("Error:", e)