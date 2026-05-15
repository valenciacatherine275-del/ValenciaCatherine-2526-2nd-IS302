# Name: Bostero, Alexa C.
def calculate_average_acb(g1_acb, g2_acb, g3_acb):
    return (g1_acb + g2_acb + g3_acb) / 3

def get_remark_acb(average_acb):
    if average_acb >= 90:
        return "Excellent"
    elif average_acb >= 85:
        return "Very Good"
    elif average_acb >= 80:
        return "Good"
    elif average_acb >= 75:
        return "Fair"
    else:
        return "Failed"

g1_acb = float(input("Enter grade 1: "))
g2_acb = float(input("Enter grade 2: "))
g3_acb = float(input("Enter grade 3: "))

average_acb = calculate_average_acb(g1_acb, g2_acb, g3_acb)
remark_acb = get_remark_acb(average_acb)

print("\n----- STUDENT GRADE REPORT -----")
print("Average:", format(average_acb, ".2f"))
print("Remark:", remark_acb)