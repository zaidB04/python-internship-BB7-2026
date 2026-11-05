#age = "20"
#next_year_age = age + 1

#print("Next year I will be " + next_year_age)
#The variable age contains "20" as a string.

#But we are trying to add 1, which is an integer.

#Python cannot directly add a string and an integer.

#Correct Code
age = "20"

# Convert string into integer
age = int(age)

next_year_age = age + 1

print("Next year I will be " + str(next_year_age))