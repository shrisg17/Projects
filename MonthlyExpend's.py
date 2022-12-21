import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('/home/shridhar/expenditure.csv')

# Create an empty list to store the subsets
expenditure_data = []

# Iterate over the rows of the DataFrame
for index, row in df.iterrows():
  # Extract the values from each column
  col1 = row["Date"]
  col2 = row["Expenditure"]
  col3 = row["Category"]

  # Create a subset using the values from the columns
  subset = (col1,col2 ,col3)

  # Add the subset to the list
  expenditure_data.append(subset)


# Create a pandas DataFrame from the expenditure data
df = pd.DataFrame(expenditure_data, columns=["Date", "Expenditure", "Category"])

# Convert the date column to a datetime data type
df["Date"] = pd.to_datetime(df["Date"])

# Group the data by category and sum the amounts
df_grouped = df.groupby("Category")["Expenditure"].sum()

# Plot the expenditure data as a bar chart
df_grouped.plot(kind="bar")

# Set the plot title and labels
plt.title("Monthly Expenditures")
plt.xlabel("Category")
plt.ylabel("Total Spend")

# Show the plot
plt.show()
