registrations = {
    "Arun": ["Python", "Java", "SQL", "Python"],
    "Bala": ["Python", "C", "SQL"],
    "Charan": ["Java", "Python", "SQL"],
    "Divya": ["Python", "Java"],
    "Ezhil": ["C", "Java", "Java"]
}
target = "Arun"
common_students = {}
target_courses = set(registrations[target])
for student, courses in registrations.items():
    if student != target:
        common = target_courses & set(courses)
        if len(common) >= 2:
            common_students[student] = sorted(common)
print("Common courses:", common_students)
