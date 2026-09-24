import sqlite3

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

cursor.execute("SELECT id, name, year_group, favourite_subject FROM students")

rows = cursor.fetchall()

print(rows)

for student_id, name, year_group, favourite_subject in rows:
    print(f"{name} is in year {year_group}, and like's {favourite_subject}.")

connection.close()