# Student Grade Calculator

# Taking input
name = input("Enter Student Name: ")
mark1 = float(input("Enter marks for Subject 1 (0-100): "))
mark2 = float(input("Enter marks for Subject 2 (0-100): "))
mark3 = float(input("Enter marks for Subject 3 (0-100): "))

# Calculating total and percentage
total = mark1 + mark2 + mark3
percentage = (total / 300) * 100

# Grade calculation using if-elif-else
if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

# Displaying output
print("\n----- Result -----")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)