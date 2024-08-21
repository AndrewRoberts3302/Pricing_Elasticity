import pandas as pd
from pathlib import Path

from i_band_shares import df

print("\nThe head of df to use for calculating class shares is:\n", df.head(2), "\n")

# Take the product level slices.

df_product = df.loc[df["product_level"] == "Product"]
# df_class = df.loc[df["product_level"] == "Product Class"]
# df_group = df.loc[df["product_level"] == "Product Group"]

print("\nThe head of df_product is:\n", df_product.head(2), "\n")
# print("\nThe head of df_class is:\n", df_class.head(2), "\n")
# print("\nThe head of df_group is:\n", df_group.head(2), "\n")

# Calculate the values for the product classes
df_product = df_product.groupby(
    [
        "market", "product_group", "uom", "price_vs_control_band"
        ]
).agg(
    {
        "quantity": ["sum"],
        "value": ["sum"]
    }
)
df_product.columns = df_product.columns.get_level_values(0)
df_product = df_product.reset_index()
df_product["product"] = df_product["product_group"]
df_product["product_class"] = df_product["product_group"]

# Calculate the values for the product classes
df_product_class = df_product.groupby(
    [
        "market", "product_class", "uom", "price_vs_control_band"
        ]
).agg(
    {
        "quantity": ["sum"],
        "value": ["sum"]
    }
)
df_product_class.columns = df_product_class.columns.get_level_values(0)
df_product_class = df_product_class.reset_index()
df_product_class = df_product_class.rename(columns={
    "quantity": "class_quantity",
    "value": "class_value"})


# Calculate the values for the product classes
df_product_group = df_product.groupby(
    [
        "market", "product_group", "uom", "price_vs_control_band"
        ]
).agg(
    {
        "quantity": ["sum"],
        "value": ["sum"]
    }
)
df_product_group.columns = df_product_group.columns.get_level_values(0)
df_product_group = df_product_group.reset_index()
df_product_group = df_product_group.rename(columns={
    "quantity": "group_quantity",
    "value": "group_value"})

# Merge the results
df_product = pd.merge(
    df_product, df_product_class,
    left_on=["market", "product_class", "uom", "price_vs_control_band"],
    right_on=["market", "product_class", "uom", "price_vs_control_band"],
    how="inner"
)

df_product = pd.merge(
    df_product, df_product_group,
    left_on=["market", "product_group", "uom", "price_vs_control_band"],
    right_on=["market", "product_group", "uom", "price_vs_control_band"],
    how="inner"
)

df_product["share_in_class_quantity"] = df_product["quantity"] / df_product["class_quantity"]
df_product["share_in_class_value"] = df_product["value"] / df_product["class_value"]
df_product["share_in_group_quantity"] = df_product["quantity"] / df_product["group_quantity"]
df_product["share_in_group_value"] = df_product["value"] / df_product["group_value"]

group_share = df_product[[
    "market", "product", "uom", "price_vs_control_band", "share_in_class_quantity", "share_in_class_value",
    "share_in_group_quantity", "share_in_group_value"]].copy()
group_share["product"] = "Product Group | " + group_share["product"]

# Concat the uom into the product
group_share["uom"] = group_share["uom"].astype(str)
group_share["product"] = group_share["product"] + " | " + df["uom"]

print(group_share.head(2))