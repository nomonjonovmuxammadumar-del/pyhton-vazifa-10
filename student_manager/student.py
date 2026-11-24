import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "students.json")


def load_students(file_path=DATA_FILE):
    if not os.path.exists(file_path):
        save_students([], file_path)
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, Exception):
        return []


def save_students(students, file_path=DATA_FILE):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(students, f, indent=4, ensure_ascii=False)


def add_student(name):
    students = load_students()
    new_id = 1 if not students else max(s["id"] for s in students) + 1
    new_student = {
        "id": new_id,
        "name": name.strip(),
        "grades": []
    }
    students.append(new_student)
    save_students(students)
    return new_student


def get_all_students():
    return load_students()


def search_student_by_name(name):
    students = load_students()
    query = name.strip().lower()
    return [s for s in students if query in s["name"].lower()]
