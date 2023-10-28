import pandas as pd
df = pd.read_csv("PPUBS_Basic_New.csv")
grouped = df.groupby("Inventor name")
group_counts = grouped.size()
print(group_counts)
group_counts.to_csv("grouped_data.csv")
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("PPUBS_Basic_New.csv")

# Group the data by a specific column (e.g., "Category")
grouped = df.groupby("Inventor name")

# Calculate the count of items in each group
group_counts = grouped.size()

# Print or save the results
print(group_counts)
# group_counts.to_csv("grouped_data.csv")
