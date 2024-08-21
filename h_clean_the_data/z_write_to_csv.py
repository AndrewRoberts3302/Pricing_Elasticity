import pandas as pd
from c_Data_Path.a_data_path import data_path

from c_remove_outliers_price import df

# Check the outlet counts in the data after cleaning.
n = len(pd.unique(df["outlet"]))
print("\nThe outlet counts in the data after cleaning is:", n, "\n")

df.to_csv(data_path / "data_clean.csv", index=False)

