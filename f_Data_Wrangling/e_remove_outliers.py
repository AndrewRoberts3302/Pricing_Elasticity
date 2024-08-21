from d_replace_qty_and_value_data import df

# Outliers can be identified by the price index.
# Data needs to have a price index within 0.75 and 1.50.

# df = df.loc[
#     (df["price_index"] >= 0.75) &
#     (df["price_index"] <= 1.50)
# ]
