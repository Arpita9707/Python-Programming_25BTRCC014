def evaluate(m1, m2, m3, attendance):
    average = (m1 + m2 + m3) / 3

    if m1 >= 40 and m2 >= 40 and m3 >= 40:
        if average >= 75 and attendance >= 75:
            return average, "Eligible"
    return average, "Not Eligible"
data = input("Enter marks and attendance: ").split()
result = evaluate(
    float(data[0]),
    float(data[1]),
    float(data[2]),
    float(data[3])
)
print("Average:", result[0])
print("Status:", result[1])