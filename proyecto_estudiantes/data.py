# data.py
import csv
import os

CSV_FILE = "estudiantes.csv"
FIELDNAMES = ['name', 'section', 'spanish', 'english', 'social', 'science', 'average']


def export_csv(students):
    if not students:
        print("\n  its empty.")
        return

    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(students)

    print(f"Successfully exported to '{CSV_FILE}'. ({len(students)} student(s))")


def import_csv(students):
    if not os.path.exists(CSV_FILE):
        print(f"\nThe file '{CSV_FILE}' does not exist. Please export the data first.")
        return

    students.clear()

    with open(CSV_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            students.append({
                'name':    row['name'],
                'section': row['section'],
                'spanish': float(row['spanish']),
                'english': float(row['english']),
                'social':  float(row['social']),
                'science': float(row['science']),
                'average': float(row['average'])
            })

    print(f" Successfully imported data from '{CSV_FILE}'. ({len(students)} student(s) loaded)")
