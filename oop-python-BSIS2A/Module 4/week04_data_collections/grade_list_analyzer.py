# Name: Bostero, Alexa C.

grades_acb = []

# Input 5 grades
for i_acb in range(5):
    grade_acb = float(input(f"Enter grade {i_acb + 1}: "))
    grades_acb.append(grade_acb)

# Compute values
average_acb = sum(grades_acb) / len(grades_acb)
highest_acb = max(grades_acb)
lowest_acb = min(grades_acb)

# Output
print("\n----- GRADE ANALYSIS -----")
print("Average Grade:", format(average_acb, ".2f"))
print("Highest Grade:", highest_acb)
print("Lowest Grade:", lowest_acb)