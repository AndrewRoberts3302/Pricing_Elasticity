import pandas as pd

from a_read_in_the_data import df
from a_read_in_the_data import data_path, data_clean


print("\nThe head of df is:\n", df.head(2), "\n")

# Check the dates in the data.

u = df["date"]. unique()
print("\nThe unique dates in the data are:\n", sorted(u), "\n")

print("\nThere should only be one date used in this project.")

# Check the outlet counts in the data before the analysis.
n = len(pd.unique(df["outlet"]))
print("\nThe outlet counts in the data after cleaning is:", n, "\n")

# Check for NaN values in the product column.
print('Checking if there are any nulls in the product column: ',
      df['product'].isnull().values.any(), '\n')

# In some data the regions can cause issues if there are zeros in from custom
# changes where conditions weren't met.

print("\nThe unique regions in the data are:\n\n")
u = df["region"].unique()
print(u)
