"""
Comment out the script if this update is not required.
"""

import pandas as pd

from f1_apply_custom_diageo_segments_OPTION import (
    df,
    df_product
    # data_product_miller_beer_quality
)

from a_read_in_the_data import custom_products

df["product_class"] = df["product_class"].astype(str)
custom_products["cmbc_product_sub_segment"] = custom_products["cmbc_product_sub_segment"].astype(str)

#######################################################################################################################
# CMBC custom product segment - used for SB169
# Comment out if not required.

# custom_products = pd.read_csv("../e_SQL_Data_Pulls/cmbc_product_data.csv")
#
# print("\nThe head of df is:\n", df.head(2), "\n")
# print("\nThe head of cmbc_product_data is:\n", custom_products.head(2), "\n")
#
# # Drop the product columns to replace.
# df = df.drop(["product_class"], axis=1)
#
# # Take only the update columns needed.
# custom_products = custom_products[["product_item_id", "cmbc_product_sub_segment"]]
#
# # Rename the update columns.
# custom_products = custom_products.rename(
#     columns={
#         "cmbc_product_sub_segment": "product_class"
#     }
# )
#
# # Merge in the updates.
#
# df = pd.merge(
#     df, custom_products,
#     left_on=["pm_product_item_id"],
#     right_on=["product_item_id"],
#     how="inner"
# )
#######################################################################################################################

#######################################################################################################################
# CMBC custom product segment - used for SB144
# Comment out if not required.

# print("\nThe head of df is:\n", df.head(2), "\n")
# print("\nThe head of cmbc_product_data is:\n", custom_products.head(2), "\n")
#
# u = df["product_class"].unique()
# print("\nThe current product_classes are:\n\n", sorted(u))
#
# # Drop the product columns to replace.
# df = df.drop(["product_class", "product_group"], axis=1)
#
# # Take only the update columns needed.
# custom_products = custom_products[["product_item_id", "cmbc_product_sub_segment", "cmbc_product_segment"]]
#
# # Rename the update columns.
# custom_products = custom_products.rename(
#     columns={
#         "cmbc_product_sub_segment": "product_class",
#         "cmbc_product_segment": "product_group"
#     }
# )
#
# # Merge in the updates.
#
# df = pd.merge(
#     df, custom_products,
#     left_on=["pm_product_item_id"],
#     right_on=["product_item_id"],
#     how="inner"
# )
#
# u = df["product_class"].unique()
# print("\nThe new product_classes are:\n\n", sorted(u))
#######################################################################################################################