name_acb = input("Enter student name: ")

grade1_acb = float(input("Enter grade 1: "))
grade2_acb = float(input("Enter grade 2: "))
grade3_acb = float(input("Enter grade 3: "))

average_acb = (grade1_acb + grade2_acb + grade3_acb) / 3

print("\nStudent:", name_acb)
print("Average:", average_acb)

if 90 <= average_acb <= 100:
    print("Remark: Excellent")
elif 85 <= average_acb <= 89:
    print("Remark: Very Good")
elif 80 <= average_acb <= 84:
    print("Remark: Good")
elif 75 <= average_acb <= 79:
    print("Remark: Fair")
else:
    print("Remark: Failed")