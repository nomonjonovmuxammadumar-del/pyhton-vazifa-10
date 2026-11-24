from student import add_student, get_all_students, search_student_by_name
from grades import add_grade, calculate_average, get_student_average, get_top_student


def print_table(students):
    if not students:
        print("\n[!] Talabalar ro'yxati bo'sh.")
        return

    print("\n" + "=" * 76)
    print(f"| {'ID':<4} | {'Talaba F.I.Sh':<25} | {'Baholari':<23} | {'O`rtacha':<8} |")
    print("=" * 76)
    for s in students:
        grades = s.get("grades", [])
        grades_str = ", ".join(map(str, grades)) if grades else "Baho yo'q"
        avg = calculate_average(grades)
        print(f"| {s['id']:<4} | {s['name']:<25} | {grades_str:<23} | {avg:<8} |")
    print("=" * 76)


def handle_add_student():
    print("\n" + "-" * 35)
    print("      YANGI TALABA QO'SHISH")
    print("-" * 35)
    name = input("Talabaning ism va familiyasini kiriting: ").strip()
    if not name:
        print("[XATO] Ism bo'sh bo'lishi mumkin emas!")
        return
    student = add_student(name)
    print(f"[MUVAFFAQIYAT] Yangi talaba qo'shildi: ID {student['id']} - {student['name']}")


def handle_show_students():
    print("\n" + "-" * 35)
    print("     BARCHA TALABALAR RO'YXATI")
    print("-" * 35)
    students = get_all_students()
    print_table(students)


def handle_search_student():
    print("\n" + "-" * 35)
    print("    ISM BO'YICHA TALABA QIDIRISH")
    print("-" * 35)
    query = input("Qidirilayotgan ismni kiriting: ").strip()
    if not query:
        print("[XATO] Qidiruv matni bo'sh bo'lmasligi kerak!")
        return
    results = search_student_by_name(query)
    if results:
        print(f"\nTopilgan talabalar ({len(results)} ta):")
        print_table(results)
    else:
        print(f"[!] '{query}' bo'yicha talaba topilmadi.")


def handle_add_grade():
    print("\n" + "-" * 35)
    print("      TALABAGA BAHO QO'SHISH")
    print("-" * 35)
    students = get_all_students()
    if not students:
        print("[!] Tizimda talabalar mavjud emas. Avval talaba qo'shing!")
        return

    print_table(students)
    try:
        student_id = int(input("\nBaho qo'shiladigan talaba ID raqamini kiriting: "))
    except ValueError:
        print("[XATO] ID faqat butun son bo'lishi kerak!")
        return

    try:
        grade_input = input("Bahoni kiriting (0 - 100): ").strip()
        grade = float(grade_input)
        if grade < 0 or grade > 100:
            print("[XATO] Baho 0 va 100 oralig'ida bo'lishi kerak!")
            return
        if grade.is_integer():
            grade = int(grade)
    except ValueError:
        print("[XATO] Baho raqam bo'lishi kerak!")
        return

    success, student = add_grade(student_id, grade)
    if success:
        print(f"[MUVAFFAQIYAT] {student['name']} ga {grade} bahosi qo'shildi.")
        print(f"Barcha baholari: {student['grades']}")
    else:
        print(f"[XATO] ID {student_id} bo'yicha talaba topilmadi!")


def handle_student_average():
    print("\n" + "-" * 35)
    print(" TALABANING O'RTACHA BAHOSINI KO'RISH")
    print("-" * 35)
    try:
        student_id = int(input("Talaba ID raqamini kiriting: "))
    except ValueError:
        print("[XATO] ID butun son bo'lishi kerak!")
        return

    student, avg = get_student_average(student_id)
    if student:
        grades_str = ", ".join(map(str, student.get("grades", []))) or "Baho yo'q"
        print("\n" + "=" * 45)
        print(f"Talaba: {student['name']} (ID: {student['id']})")
        print(f"Baholari: [{grades_str}]")
        print(f"O'rtacha baho: {avg}")
        print("=" * 45)
    else:
        print(f"[XATO] ID {student_id} bo'yicha talaba topilmadi!")


def handle_top_student():
    print("\n" + "-" * 35)
    print("    ENG YUQORI BAHO OLGAN TALABA")
    print("-" * 35)
    top_student, highest_avg = get_top_student()
    if top_student:
        grades_str = ", ".join(map(str, top_student.get("grades", [])))
        print("\n" + "*" * 48)
        print("🏆 ENG YUQORI NATIJAGA EGA TALABA:")
        print(f"   F.I.Sh: {top_student['name']} (ID: {top_student['id']})")
        print(f"   Baholari: [{grades_str}]")
        print(f"   O'rtacha bali: {highest_avg}")
        print("*" * 48)
    else:
        print("[!] Bahoga ega talaba mavjud emas.")


def main():
    while True:
        print("\n" + "=" * 55)
        print("    TALABALAR VA ULARNING BAHOLARINI BOSHQARISH")
        print("=" * 55)
        print("1. Talaba qo'shish")
        print("2. Barcha talabalarni ko'rish")
        print("3. Ism bo'yicha talaba qidirish")
        print("4. Talabaning bahosini qo'shish")
        print("5. Talabaning o'rtacha bahosini hisoblash")
        print("6. Eng yuqori baho olgan talabani aniqlash")
        print("0. Dasturdan chiqish")
        print("=" * 55)

        choice = input("Tanlovingizni kiriting (0-6): ").strip()

        if choice == "1":
            handle_add_student()
        elif choice == "2":
            handle_show_students()
        elif choice == "3":
            handle_search_student()
        elif choice == "4":
            handle_add_grade()
        elif choice == "5":
            handle_student_average()
        elif choice == "6":
            handle_top_student()
        elif choice == "0":
            print("\nDastur yakunlandi. Salomat bo'ling!")
            break
        else:
            print("\n[XATO] Noto'g'ri tanlov kiritildi! 0 dan 6 gacha bo'lgan raqamni tanlang.")


if __name__ == "__main__":
    main()
