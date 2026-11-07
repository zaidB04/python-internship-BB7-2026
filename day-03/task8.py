tasks = []

# Add 5 tasks
tasks.append("Study Python")
tasks.append("Practice c")
tasks.append("Learn dsa")
tasks.append("Complete css")
tasks.append("Exercise")

print("Current Tasks:")
print(tasks)

# Remove 2 tasks
tasks.remove("Practice c")
tasks.remove("Exercise")

print("\nUpdated To-Do List:")

for task in tasks:
    print("-", task)