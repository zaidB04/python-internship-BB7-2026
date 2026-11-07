students = [
    ("ajay", 88),
    ("vijay", 95),
    ("karan", 72),
    ("Arjun", 85)
]

students.sort(key=lambda x: x[1], reverse=True)

print("Students Sorted by Marks:")

for name, marks in students:
    print(name, marks)