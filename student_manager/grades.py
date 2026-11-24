from student import load_students, save_students


def add_grade(student_id, grade):
    students = load_students()
    for student in students:
        if student["id"] == student_id:
            student["grades"].append(grade)
            save_students(students)
            return True, student
    return False, None


def calculate_average(grades):
    if not grades:
        return 0.0
    return round(sum(grades) / len(grades), 2)
