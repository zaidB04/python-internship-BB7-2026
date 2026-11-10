class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __eq__(self, other):
        return self.width * self.height == other.width * other.height


r1 = Rectangle(4, 6)
r2 = Rectangle(3, 8)

if r1 == r2:
    print("Both rectangles are equal.")
else:
    print("Rectangles are not equal.")

print("Rectangle 1 Area:", r1.width * r1.height)
print("Rectangle 2 Area:", r2.width * r2.height)