from pathlib import Path
import pandas as pd

from a_read_in_the_data import df, df_data

print("\n-------------------------------------------------------------------\n")
print("RUNNING FILE: ", Path(__file__).name)
print("\n-------------------------------------------------------------------\n")

print("\nThe head of the supplied pricing data df is:\n", df.head(2), "\n")

# Check the data types in the pricing data.
print("\nThe dtypes in the supplied pricing data are:\n", df.dtypes, "\n")

# Reformat any columns that need it.
# Remove commas from the 'SumOfSumOfF_SalesValue_' column
df["SumOfSumOfF_SalesValue_"] = df["SumOfSumOfF_SalesValue_"].str.replace(',', '')

# Convert the 'SumOfSumOfF_SalesValue_' column to numeric
df["SumOfSumOfF_SalesValue_"] = pd.to_numeric(df["SumOfSumOfF_SalesValue_"], errors='coerce')

print("\nThe head of the Epos data df_data is:\n", df_data.head(2))

