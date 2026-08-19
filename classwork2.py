import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "mashup"

df_dict = pd.DataFrame({
    "Name": ["Asha", "Ravi", "Meera"],
    "Age": [24, 30, 26],
    "Dept": ["HR", "IT", "Finance"]
})
print(" DataFrame from dictionary:")
print(df_dict)
print()
student = pd.read_csv(DATA_DIR / "student.csv")
print("Student Data (CSV):")
print(student)
print()
employee = pd.read_excel(DATA_DIR / "employee.xlsx")
print(" Employee Data (Excel):")
print(employee)
print()
mash = pd.read_json(DATA_DIR / "mash.json")
print(" JSON Data:")
print(mash)