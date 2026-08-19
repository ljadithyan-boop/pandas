import pandas as pd
import sqlite3
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "mashup"

data = [
    ["Ammu", 23, "Python"],
    ["manu", 25, "Django"],
    ["Anu", 22, "React"]
]

df_list = pd.DataFrame(
    data,
    columns=["Name", "Age", "Course"],
    index=["S1", "S2", "S3"]
)

print("TASK 1: DataFrame from List")
print(df_list)
print()
data = [
    ("Pen", 10),
    ("Book", 50),
    ("Bag", 700)
]

df_tuples = pd.DataFrame(
    data,
    columns=["Item", "Price"]
)

print("TASK 2: DataFrame from Tuples")
print(df_tuples)
print()

df_marks = pd.read_csv(
    DATA_DIR / "marks.txt",
    sep="|",
    header=None,
    names=["ID", "Name", "Mark"]
)

print("TASK 3: Marks DataFrame")
print(df_marks)
print()
df_employees = pd.read_excel(
    DATA_DIR / "employees.xlsx",
    usecols=["Name", "Salary"]
)

print("TASK 4: Employees DataFrame")
print(df_employees)
print()

df_students = pd.read_json(DATA_DIR / "data.json")

df_grade_a = df_students[df_students["Grade"] == "A"]

print("TASK 5: Students with Grade A")
print(df_grade_a)
print()
connection = sqlite3.connect(DATA_DIR / "school.db")
connection.execute("""
CREATE TABLE IF NOT EXISTS students (
    ID INTEGER,
    Name TEXT,
    Grade TEXT
)
""")
connection.execute("DELETE FROM students")
connection.execute(
    "INSERT INTO students VALUES (?, ?, ?)",
    (1, "Arun", "A")
)

connection.execute(
    "INSERT INTO students VALUES (?, ?, ?)",
    (2, "Binu", "B")
)

connection.execute(
    "INSERT INTO students VALUES (?, ?, ?)",
    (3, "Chitra", "A")
)
connection.commit()
df_sql = pd.read_sql(
    "SELECT * FROM students",
    connection
)

print("TASK 6: Students from SQLite")
print(df_sql)
connection.close()