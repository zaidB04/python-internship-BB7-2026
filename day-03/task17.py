students = [
    {"name": "ajay", "marks": 90},
    {"name": "vijay", "marks": 99},
    {"name": "karan", "marks": 82},
    {"name": "Arjun", "marks": 71}
]

topper = students[0]

for student in students:

    if student["marks"] > topper["marks"]:
        topper = student

print("Topper Name:", topper["name"])
print("Highest Marks:", topper["marks"])