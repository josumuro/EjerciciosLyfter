
import re


def is_valid_name(name):
    if not name.strip():
        return False
    if any(char.isdigit() for char in name):
        return False
    return True


def is_valid_section(section):
    """ Ej: 10A, 11B"""
    return bool(re.match(r'^\d{2}[A-Z]$', section.upper()))


def student_exists(students, name, section):
    for s in students:
        if s['name'].lower() == name.lower() and s['section'].upper() == section.upper():
            return True
    return False


def get_valid_grade(subject):
    while True:
        try:
            grade = float(input(f"  Nota de {subject}: "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("The grade must be between 0-100")
        except ValueError:
            print( "Please enter a valid number.")



def add_student(students):
    print("\n--- ADD STUDENT ---")

    # Validar nombre
    while True:
        name = input("Full Name: ").strip()
        if not is_valid_name(name):
            print("Invalid name. It cannot be empty or contain numbers.")
        else:
            break

    # Validar sección
    while True:
        section = input("Section (e.g., 10A, 11B): ").strip().upper()
        if not is_valid_section(section):
            print(" Invalid section. Format: two digits + uppercase letter (e.g., 10A).")
        else:
            break

    # Verificar duplicados
    if student_exists(students, name, section):
        print(f"The student '{name}' in section '{section}' already exists.")
        return

    # Obtener notas válidas
    print("Please enter the grades (0 - 100):")
    spanish = get_valid_grade("Spanish")
    english = get_valid_grade("English")
    social  = get_valid_grade("Social Studies")
    science = get_valid_grade("Science")

    student = {
        'name':    name,
        'section': section,
        'spanish': spanish,
        'english': english,
        'social':  social,
        'science': science,
        'average': round((spanish + english + social + science) / 4, 2)
    }

    students.append(student)
    print(f" '{name}' added correctly. Average: {student['average']}")


def view_students(students):
    if not students:
        print("\n  No students registered.")
        return

    print(f"\n{'='*65}")
    print(f"{'NAME':<25} {'SECTION':<10} {'SPA':>5} {'ENG':>5} {'SOC':>5} {'SCI':>5} {'AVG':>6}")
    print(f"{'='*65}")
    for s in students:
        print(f"{s['name']:<25} {s['section']:<10} {s['spanish']:>5} {s['english']:>5} {s['social']:>5} {s['science']:>5} {s['average']:>6}")
    print(f"{'='*65}")
    print(f"Total: {len(students)} student(s)")


def top_3_students(students):
    if not students:
        print("\n No students registered.")
        return

    sorted_students = sorted(students, key=lambda x: x['average'], reverse=True)
    top = sorted_students[:3]

    medals = ["1", "2", "3"]
    print("\nTOP 3 ESTUDIANTES")
    print(f"{'='*45}")
    for i, s in enumerate(top, 1):
        print(f"{medals[i-1]} {i}. {s['name']} | {s['section']} | Average: {s['average']}")


def average_grade(students):
    if not students:
        print("\n  No students registered.")
        return

    total = sum(s['average'] for s in students)
    general_avg = round(total / len(students), 2)
    print(f"\n General average grade among all students: {general_avg}")


def delete_student(students):
    if not students:
        print("\n  No students registered.")
        return

    print("\n--- Delete Student ---")
    name    = input("Full Name: ").strip()
    section = input("Section: ").strip().upper()

    found = None
    for i, s in enumerate(students):
        if s['name'].lower() == name.lower() and s['section'] == section:
            found = (i, s)
            break

    if not found:
        print(f" No student found with the name '{name}' in section '{section}'.")
        return

    idx, student = found
    print(f"\nAre you sure you want to delete '{student['name']}' from section '{student['section']}'?")
    confirm = input("Confirm (y/n): ").strip().lower()

    if confirm == 'y':
        students.pop(idx)
        print(f" '{student['name']}' deleted successfully.")
    else:
        print("Operation cancelled.")


def view_failed_students(students):
    if not students:
        print("\n No students registered.")
        return

    subjects = {
        'spanish': 'Español',
        'english': 'Inglés',
        'social':  'Sociales',
        'science': 'Ciencias'
    }

    failed = []
    for s in students:
        failed_subjects = {
            label: s[key]
            for key, label in subjects.items()
            if s[key] < 60
        }
        if failed_subjects:
            failed.append((s, failed_subjects))

    if not failed:
        print("\n No failed students.")
        return

    print(f"\n{'='*55}")
    print("📋 FAILED STUDENTS")
    print(f"{'='*55}")
    for s, fs in failed:
        print(f"\n👤 {s['name']} | Section: {s['section']}")
        for subject, grade in fs.items():
            print(f"{subject}: {grade}")
    print(f"\nTotal failed: {len(failed)}")
