import csv
import pandas as pd

lang_counts = {}
total_hours = 0
count = 0

# Read my_survey.csv using csv library
with open("my_survey.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        lang = row["FavoriteLanguage"]
        hrs = float(row["HoursCoding"])

        lang_counts[lang] = lang_counts.get(lang, 0) + 1
        total_hours += hrs
        count += 1

# Create language_counts.csv using csv library
with open("language_counts.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["FavoriteLanguage", "Count"])
    writer.writeheader()

    for lang, c in lang_counts.items():
        writer.writerow({"FavoriteLanguage": lang, "Count": c})

print("CSV file created: language_counts.csv")

# Now load that same csv using pandas
df = pd.read_csv("language_counts.csv")

print("\n--- Pandas Reading language_counts.csv ---")
print(df)

print("\nMost Popular Language:", df.loc[df["Count"].idxmax(), "FavoriteLanguage"])
