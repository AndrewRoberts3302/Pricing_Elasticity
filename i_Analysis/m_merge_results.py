import pandas as pd

from g_1_product_ros import ros
from h_band_shares import band_share
from l_append_shares import shares
from g_2_product_nda_share import dp

print("\nMerging the result dataframes.\n")
print("\nThe head of ros is:\n", ros.head(2), "\n")
print("\nThe head of band_share is:\n", band_share.head(2), "\n")
print("\nThe head of shares is:\n", shares.head(2), "\n")
print("\nThe head of nda share data dp is:\n", dp.head(2))

results = pd.merge(
    ros, band_share,
    left_on=["date", "market", "product", "uom", "price_band"],
    right_on=["date", "market", "product", "uom", "price_band"],
    how="inner"
)

results = pd.merge(
    results, shares,
    left_on=["market", "product", "uom", "price_band"],
    right_on=["market", "product", "uom", "price_band"],
    how="inner"
)

results = pd.merge(
    results, dp,
    left_on=["date", "market", "product", "uom", "price_band"],
    right_on=["date", "market", "product", "uom", "price_band"],
    how="inner"
)

print("\nThe head of results after merging in the results is:\n", results.head(2), "\n")
