employees = {
    "Ajay": 35000,
    "vijay": 65000,
    "karan": 45000,
    "Arjun": 70000,
    "mala": 75000
}

sorted_employees = sorted(
    employees.items(),
    key=lambda x: x[1],
    reverse=True
)

print("Top 3 Highest Paid Employees:")

for name, salary in sorted_employees[:3]:

    print(name, ":", salary)