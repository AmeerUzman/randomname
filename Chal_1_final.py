import csv
import pandas as pd

students = []

# STEP 1: Read the original file with pandas
df = pd.read_csv("students_grades.csv")

# Calculate average quiz score
df["Average"] = df[["Quiz1", "Quiz2", "Quiz3"]].fillna(0).mean(axis=1).round(2)

# Convert pandas rows → python dicts (for csv writing)
students = df[["Name", "Average"]].to_dict(orient="records")

# STEP 2: Create averages.csv using CSV LIBRARY
with open("averages.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Name", "Average"])
    writer.writeheader()
    writer.writerows(students)

print("CSV file created: averages.csv")

# STEP 3: Load averages.csv using pandas
df2 = pd.read_csv("averages.csv")

# STEP 4: Use pandas to print top 3 students
print("\nTop 3 Students (Pandas using averages.csv):")
top3 = df2.nlargest(3, "Average")

for _, row in top3.iterrows():
    print(row["Name"], row["Average"])
