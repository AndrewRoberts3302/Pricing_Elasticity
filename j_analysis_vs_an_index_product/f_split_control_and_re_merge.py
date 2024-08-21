import pandas as pd

from e_identify_product_RUN_THIS_TO_IDENTIFY_PRODUCTS import df

# Check the outlet counts in the data before splitting and remerging.
n = len(pd.unique(df["outlet"]))
print("\nThe outlet counts in the data before splitting and re-merging is:", n, "\n")

print("\nThe head of df is:\n", df.head(2))

print("Describing the data before splitting and remerging")
print(df.describe())

co = df.loc[df["is_control_product"] == 1]

co = co[["date", "outlet", "uom", "price", "quantity", "value"]].drop_duplicates()

co = co.rename(columns={
    "price": "control_price",
    "quantity": "control_quantity",
    "value": "control_value"
})

df = pd.merge(
    df, co,
    left_on=["date", "outlet", "uom"],
    right_on=["date", "outlet", "uom"],
    how="inner"
)

df["price_vs_control"] = df["price"] - df["control_price"]

# Check the outlet counts in the data after splitting and remerging.

print("Describing the data after splitting and remerging")
print(df.describe())

n = len(pd.unique(df["outlet"]))
print("\nThe outlet counts in the data after splitting and re-merging is:", n, "\n")