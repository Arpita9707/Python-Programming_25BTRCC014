names = ["Anu", "Bharath", "Chitra", "Deepak", "Farah"]
attendance = [92, 68, 85, 45, 78]
marks = [88, 55, 76, 32, 91]
eligible_students = 0
for student_no, (name, att, mark) in enumerate(zip(names, attendance, marks), start=1):
    if att < 0 or att > 100 or mark < 0 or mark > 100:
        print(f"Invalid data for {name} - Skipped")
        continue
    if att >= 75:
        eligible_students += 1
        if 80 <= mark <= 100:
            result = "Distinction"
        elif 60 <= mark <= 79:
            result = "First Class"
        elif 40 <= mark <= 59:
            result = "Pass"
        else:
            result = "Fail"
        print(f"{student_no}. {name} - Attendance: {att}% - Marks: {mark} - {result}")
    else:
        print(f"{student_no}. {name} - Attendance: {att}% - Not Eligible")
print(f"\nTotal Eligible Students: {eligible_students}")