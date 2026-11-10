def make_counter():

    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


counter1 = make_counter()
counter2 = make_counter()


print("Counter 1:", counter1())
print("Counter 1:", counter1())
print("Counter 1:", counter1())

print("Counter 2:", counter2())
print("Counter 2:", counter2())

print("Final Counter 1:", counter1())
print("Final Counter 2:", counter2())