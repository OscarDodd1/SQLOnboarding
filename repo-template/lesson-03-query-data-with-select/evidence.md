# Lesson 03 Evidence Pro-Forma

## Commit evidence (minimum 2)
- Commit 1 hash + message: c4910da - Finished lesson 3 code
-Finished lesson 3 code
- Commit 2 hash + message:
- Optional Commit 3 hash + message:

## Run evidence
- Command run: lesson3_select.py
- Terminal output pasted below:
(1, 'Adrian', 10)
(2, 'Leo', 11)
(3, 'Leroy', 12)

## Typed-work confirmation
- Briefly describe how you typed your changes step-by-step (including at least one pause to run and check output): I typed each line in from the lesson, then added to the execute function by adding in a column from a previous lesson.

## Prediction before run
- Query version:
- My prediction (rows/columns or sample output): it will print out 4 rows with, the student id, name, year group and their favourite subject.
- What actually happened: it printed out my prediction.

## SQL/Python changes I made
- Change 1: Added another column to get from cursor.execute()
- Change 2: Added a cleaner output.
- Why these changes were mine (not just starter code): the favourite_subject column is from the previous lesson.

## Error and fix
- Error I hit: for student_id, name, year_group in rows:
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: too many values to unpack (expected 3)
- How I fixed it: I added favourite_subject to the for loop.

## Understanding check (answer in your own words)
1. What is the job of `SELECT`?
- "SELECT" retrieves data from a database.
2. What type of value does `fetchall()` return?
- fetchall() returns a single list of all data from a database.
3. How did your output change when you selected fewer columns?
- When I selected less colums the output also had less columns because fetchall() doesnt retrieve them.

## Quality checklist
- [X] Script runs without unhandled errors
- [X] I included at least 2 lesson commits
- [X] I included query output evidence
- [X] I showed a prediction and compared it to actual output
- [X] I made at least 2 personal changes to the starter work
- [X] I answered all questions in my own words
