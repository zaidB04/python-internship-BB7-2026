def require_positive(func):

    def wrapper(a, b):

        if a <= 0 or b <= 0:
            print("Error: Both numbers must be positive!")
            return

        return func(a, b)

    return wrapper


@require_positive
def divide(a, b):

    print("Division:", a / b)


divide(40, 8)

divide(-80, 3)

divide(10, 0)