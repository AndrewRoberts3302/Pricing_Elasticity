import pandas as pd

from k_aggregate_outlet_regions_OPTION import (
    df,
    df_product
    # data_product_miller_beer_quality
)

print("\nThe head of df before updating the product data is:\n", df.head(2), "\n")

print("\nThe head of df_product for updating df is:\n", df_product.head(2), "\n")

u = df_product["product_class"].unique()
print("\nThe unique product_class data in the product data is:\n\n", u)

u = df_product["product_group"].unique()
print("\nThe unique product_group data in the product data is:\n\n", u)

################################################################################
# Drop the product columns to be replaced.
#
# This is the usual script to use by default

# df = df.drop(["product_class", "product_group"], axis=1)
# df_product = df_product.drop(["product"], axis=1)
#
# # Merge in the updates.
# df = pd.merge(
#     df, df_product,
#     left_on=["pm_product_item_id"], right_on=["pm_product_item_id"],
#     how="inner"
# )
################################################################################

################################################################################
# # Drop the product columns in the df table that will be replaced.
# df = df.drop(["product_group"], axis=1)
#
# # Drop the product columns in the product table that won't be used as updates.
# df_product = df_product.drop(["product", "product_class"], axis=1)
#
#
#
# # Merge in the updates.
# df = pd.merge(
#     df, df_product,
#     left_on=["pm_product_item_id"], right_on=["pm_product_item_id"],
#     how="inner"
# )
################################################################################

################################################################################
# Use the Miller product qualities.

# Drop the product columns in the df table that will be replaced.
# df = df.drop(["product_class", "product_group"], axis=1)
#
# # Drop the product columns in the product table that won't be used as updates.
# data_product_miller_beer_quality = data_product_miller_beer_quality.drop(["product"], axis=1)
#
# # Merge in the updates.
# df = pd.merge(
#     df, data_product_miller_beer_quality,
#     left_on=["pm_product_item_id"], right_on=["pm_product_item_id"],
#     how="inner"
# )
################################################################################

print("\nThe head of df after updating the product columns is:\n", df.head(2), "\n")
