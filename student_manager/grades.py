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


def get_student_average(student_id):
    students = load_students()
    for student in students:
        if student["id"] == student_id:
            avg = calculate_average(student.get("grades", []))
            return student, avg
    return None, 0.0


def get_top_student():
    students = load_students()
    if not students:
        return None, 0.0

    top_student = None
    highest_avg = -1.0

    for student in students:
        grades = student.get("grades", [])
        if grades:
            avg = calculate_average(grades)
            if avg > highest_avg:
                highest_avg = avg
                top_student = student

    if top_student is not None:
        return top_student, highest_avg
    return None, 0.0
