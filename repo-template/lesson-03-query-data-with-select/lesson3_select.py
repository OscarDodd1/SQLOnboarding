import sqlite3

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

cursor.execute("SELECT id, name, year_group, favourite_subject FROM students")

rows = cursor.fetchall()

for student_id, name, year_group, favourate_subject in rows:
    print(f"{name} is in year {year_group}.")

connection.close()