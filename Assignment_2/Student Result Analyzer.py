names = ["Arun", "Bala", "Charan", "Divya", "Esha"]
marks = [85, 72, 38, 105, 91]
valid_students = 0
for student_no, (name, mark) in enumerate(zip(names, marks), start=1):
    if mark < 0 or mark > 100:
        print(f"Invalid marks for {name} - Skipped")
        continue
    if 80 <= mark <= 100:
        grade = "Excellent"
    elif 60 <= mark <= 79:
        grade = "Good"
    elif 40 <= mark <= 59:
        grade = "Average"
    else:
        grade = "Fail"
    print(f"{student_no}. {name} - {mark} - {grade}")
    valid_students += 1
print(f"\nTotal Valid Students: {valid_students}")