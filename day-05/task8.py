class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def study(self):
        print(self.name, "is studying", self.course)


s1 = Student("Zaid", 21, "BCA")

print("Name:", s1.name)
print("Age:", s1.age)
print("Course:", s1.course)

s1.study()