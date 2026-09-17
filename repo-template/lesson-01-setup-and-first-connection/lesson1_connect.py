"""Lesson 1: Connect to a SQLite database file."""

import sqlite3

print("Connects to the database file and creates one if there isnt, then it will close the connection")
print("If the file is deleted it creates a new one")

# Open a connection to school.db (SQLite creates the file if needed).
connection = sqlite3.connect("school.db") #if there isnt a school.db it will create one
print("Database connected!")

# Close the connection so the file is safely released.
connection.close()
print("Database closed!")