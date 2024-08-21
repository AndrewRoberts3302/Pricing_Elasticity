import pandas as pd
from c_Data_Path.a_data_path import data_path

# Set the console to display full contents of a DataFrame
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.width', None)

# This is now imported instead.
# df = pd.read_csv("../d_If_Using_Data_Extract_From_James/prices_table_to_use.csv", parse_dates=["D_DateKey"], encoding='latin-1', low_memory=False)

# Read in the data.
data = "data.csv"
df_data = pd.read_csv(f"{data_path}/{data}")

# Import the pricing data.
from d_If_Using_Data_Extract_From_James.a_read_in_supplied_data_and_select_date_to_use_EDIT import df