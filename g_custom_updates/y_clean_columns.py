import pandas as pd

from l_update_product_data_OPTION import df

# Check the outlet counts in the data after merging in any custom data.
n = len(pd.unique(df["outlet"]))
print("\nThe outlet counts in the data after merging in custom outlet data is:", n, "\n")

# Check the head of the data.
print("\nThe head of df after custom merges are complete is:\n", df.head(2), "\n")

# Select the columns required.
df = df[[
    "date",
    "outlet",
    "operator",
    "outlet_brand",
    "segment",
    "region",
    "is_london",
    "quality",
    "data_partner",
    "product",
    "product_class",
    "product_group",
    "uom",
    "price",
    "quantity",
    "value",
    "volume"
    ]]

# Check the row count after cleaning the data ready for export.
print(
    "\nThe shape of the data after cleaning the data ready for export is:\n",
    df.shape
)
print(df.head(10))

u = df["product_class"].unique()
print("\nThe unique product_class in df are now:\n\n", sorted(u))