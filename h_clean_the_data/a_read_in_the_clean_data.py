import pandas as pd
from c_Data_Path.a_data_path import data_path

# Set the console to display full contents of a DataFrame
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.width', None)

# Read in the data
data_custom = "data_custom.csv"
df = pd.read_csv(f"{data_path}/{data_custom}", parse_dates=["date"])

# Check the outlet counts in the data before cleaning.
n = len(pd.unique(df["outlet"]))
print("\nThe outlet counts in the data before cleaning is:", n, "\n")
