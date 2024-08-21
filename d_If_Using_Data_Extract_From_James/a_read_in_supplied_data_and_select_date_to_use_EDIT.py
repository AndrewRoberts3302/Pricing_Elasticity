import pandas as pd
from pathlib import Path
from c_Data_Path.a_data_path import data_path

print("\n-------------------------------------------------------------------\n")
print("RUNNING FILE: ", Path(__file__).name)
print("\n-------------------------------------------------------------------\n")

################################################################################
# EDIT: Select the data to use:
################################################################################
# prices_table_to_use = "prices_table_to_use.csv"
# prices_table_to_use = "prices_table_to_use_FEB_2024.csv"
# prices_table_to_use = "prices_table_to_use_feb_24_feb_23.csv"
prices_table_to_use = "prices_table_july_2024.csv"

################################################################################

df = pd.read_csv(f"{data_path}/{prices_table_to_use}", parse_dates=["D_DateKey"], encoding='latin-1', low_memory=False)

################################################################################

# Check how many dates are in the data.

u = df["D_DateKey"].unique()

print("\nThe unique dates in the supplied pricing data are:\n\n", u)
print("\nYou must use only date in the process, you can select it in this file.\n\n")

# Select the date to use.

df = df.loc[df["D_DateKey"] == "13/07/2024"]

u = df["D_DateKey"].unique()

print("\nThe date selected to use is:\n\n", u)


