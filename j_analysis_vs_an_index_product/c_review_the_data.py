import pandas as pd

from b_read_in_the_data import df

df.loc[(df['product_group'] == 'LAD') & (df['uom'] == 'Pint'), 'product'] = 'Draught LAD'

print("\nThe head of df is:\n", df.head(2), "\n")

# Check the dates in the data.

u = df["date"]. unique()
print("\nThe unique dates in the data are:\n", sorted(u), "\n")

print("\nThere is only one date used in this project.")

# Check the outlet counts in the data before the analysis.
n = len(pd.unique(df["outlet"]))
print("\nThe outlet counts in the data after cleaning is:", n, "\n")

# Check for NaN values in the product column.
print('Checking if there are any nulls in the product column: ',
      df['product'].isnull().values.any(), '\n')

# Remove the product rows with NaN values
df = df.dropna(subset=["product"]).copy()