class InvalidAgeError(Exception):
    pass


def register_user(age):

    if age < 0 or age > 120:
        raise InvalidAgeError("Age must be between 0 and 120!")

    print("Registration Successful!")


try:
    register_user(50)
    register_user(300)

except InvalidAgeError as e:
    print("Error:", e)