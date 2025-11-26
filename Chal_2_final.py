import csv
import pandas as pd

csv_rows = []
region_sum = {}

# Read sales.csv using csv library

with open("sales.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Convert revenue to float
        row["Revenue"] = float(row["Revenue"])
        csv_rows.append(row)

        # Sum revenue by region
        region = row["Region"]
        region_sum[region] = region_sum.get(region, 0) + row["Revenue"]

# Convert totals to list of dictionaries
region_totals = [{"Region": r, "TotalRevenue": total} for r, total in region_sum.items()]

#Create region_summary.csv using CSV LIBRARY
with open("region_summary.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Region", "TotalRevenue"])
    writer.writeheader()
    writer.writerows(region_totals)

print("CSV file created: region_summary.csv")

#Load region_summary.csv using pandas
summary_df = pd.read_csv("region_summary.csv")

#Load full sales.csv into pandas to find highest sale
df_sales = pd.DataFrame(csv_rows)
max_row = df_sales.loc[df_sales["Revenue"].idxmax()]

#Use pandas to display results
print("\n--- Region Summary (Pandas) ---")
print(summary_df.sort_values("TotalRevenue", ascending=False))

print("\nHighest Single Item Sale:")
print(max_row["Region"], max_row["Item"], max_row["Revenue"])
