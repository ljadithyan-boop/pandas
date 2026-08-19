import pandas as pd
df_dict = pd.DataFrame({
    "Name": ["Asha", "Ravi", "Meera"],
    "Age": [24, 30, 26],
    "Dept": ["HR", "IT", "Finance"]
})
print(" DataFrame from dictionary:")
print(df_dict)
print()
student = pd.read_csv(r"C:\Users\Adithyan\OneDrive\Desktop\mashup\student.csv")
print("Student Data (CSV):")
print(student)
print()
employee = pd.read_excel(r"C:\Users\Adithyan\OneDrive\Documents\employee.xlsx")
print(" Employee Data (Excel):")
print(employee)
print()
mash = pd.read_json(r"C:\Users\Adithyan\OneDrive\Desktop\mashup\mash.json")
print(" JSON Data:")
print(mash)