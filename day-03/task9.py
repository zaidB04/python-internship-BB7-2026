def student_marks(marks):

    lowest = min(marks)
    highest = max(marks)
    average = sum(marks) / len(marks)

    return (lowest, highest, average)


marks = [99, 90, 92, 65, 95, 98]

result = student_marks(marks)

lowest, highest, average = result

print("Lowest Marks:", lowest)
print("Highest Marks:", highest)
print("Average Marks:", average)