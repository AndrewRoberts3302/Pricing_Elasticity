from pathlib import Path
import numpy as np

from l_update_product_data_OPTION import df

print("\n-------------------------------------------------------------------\n")
print(Path(__file__).name)
print("\n-------------------------------------------------------------------\n")

print("\nThe head of df is:\n\n", df.head(2))

u = df["region"].unique()

print("\nThe unique regions in df are:\n\n", sorted(u))

# conditions = [
#     (df["region"] == "Central"),
#     (df["region"] == "East"),
#     (df["region"] == "Lancashire"),
#     (df["region"] == "London"),
#     (df["region"] == "North East"),
#     (df["region"] == "Scotland"),
#     (df["region"] == "South & South East"),
#     (df["region"] == "South West"),
#     (df["region"] == "Wales"),
#     (df["region"] == "Yorkshire")
# ]
# choices = [
#     "North",
#     "North",
#     "North",
#     "South",
#     "North",
#     "North",
#     "South",
#     "South",
#     "North",
#     "North"
#     ]
#
# df["region"] = np.select(conditions, choices)
#
# u = df["region"].unique()
# print("\nThe unique regions in df are now:\n\n", sorted(u))
