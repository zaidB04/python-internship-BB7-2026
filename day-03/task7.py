employees = ["vijay", "Riya", "karan", "Arjun"]

salaries = [25000, 30000, 28000, 35000]

for name, salary in zip(employees, salaries):
    print("Employee:", name, "| Salary:", salary)