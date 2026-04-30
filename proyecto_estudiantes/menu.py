# menu.py
from actions import (
    add_student, view_students, top_3_students,
    average_grade, delete_student, view_failed_students
)
from data import export_csv, import_csv

students = []


def show_menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add student")
        print("2. View all students")
        print("3. View top 3 students")
        print("4. View overall average grade")
        print("5. Export to CSV")
        print("6. Import from CSV")
        print("7. Delete student")
        print("8. View failed students")
        print("0. Exit")

        option = input("\nSelect an option: ").strip()

        if option == "1":
            add_student(students)
        elif option == "2":
            view_students(students)
        elif option == "3":
            top_3_students(students)
        elif option == "4":
            average_grade(students)
        elif option == "5":
            export_csv(students)
        elif option == "6":
            import_csv(students)
        elif option == "7":
            delete_student(students)
        elif option == "8":
            view_failed_students(students)
        elif option == "0":
            print("¡Goodbye!")
            break
        else:
            print(" Invalid option. Please enter a number from 0 to 8.")
