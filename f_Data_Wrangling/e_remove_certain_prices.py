import pandas as pd

from d_replace_qty_and_value_data import df

print("\nThe shape of df before removing certain prices is:\n", df.shape, "\n")

# df = df.loc[
#
#     (df["price_index"] >= 0.75) &
#
#     (df["price_index"] <= 1.50)
#
# ]
#
# print("\nThe shape of df after removing certain prices is:\n", df.shape, "\n")