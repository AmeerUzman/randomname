import csv
import pandas as pd

n = int(input("How many responses? "))
# Create the CSV using csv module
with open("my_survey.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Name", "FavoriteLanguage", "HoursCoding"])
    writer.writeheader()

    for i in range(n):
        name = input("Name: ")
        lang = input("Favorite Language: ")
        hours = input("Hours Coding: ")

        writer.writerow({
            "Name": name,
            "FavoriteLanguage": lang,
            "HoursCoding": hours
        })

print("\nCSV file created: my_survey.csv")

# Now load that same CSV with pandas
df = pd.read_csv("my_survey.csv")

# Convert HoursCoding to numbers for analysis
df["HoursCoding"] = pd.to_numeric(df["HoursCoding"], errors="coerce").fillna(0)

# Pandas analysis
print("\n--- Pandas Summary ---")
print("Average Hours Coding:", round(df["HoursCoding"].mean(), 2))
print("Most Popular Language:", df["FavoriteLanguage"].mode()[0])

df.to_csv("my_survey_cleaned.csv", index=False)
print("\nCleaned file saved as my_survey_cleaned.csv")
