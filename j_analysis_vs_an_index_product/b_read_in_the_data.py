import pandas as pd
from c_Data_Path.a_data_path import data_path

# Set the console to display full contents of a DataFrame
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.width', None)

# Read in the data.
intermediate_analysis_df = "intermediate_analysis_df.csv"
df = pd.read_csv(f"{data_path}/{intermediate_analysis_df}", parse_dates=["date"])
