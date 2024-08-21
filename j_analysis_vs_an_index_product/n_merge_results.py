import pandas as pd

from h_1_product_ros import ros
from i_band_shares import band_share
from m_append_shares import shares
from h_2_nda_share import dp

print("\nMerging the result dataframes.\n")
print("\nThe head of ros is:\n", ros.head(2), "\n")
print("\nThe head of band_share is:\n", band_share.head(2), "\n")
print("\nThe head of shares is:\n", shares.head(2), "\n")
print("\nThe head of the nda shares data is:\n\n", dp.head(2))

results = pd.merge(
    ros, band_share,
    left_on=["date", "market", "product", "uom", "price_vs_control_band"],
    right_on=["date", "market", "product", "uom", "price_vs_control_band"],
    how="inner"
)

results = pd.merge(
    results, shares,
    left_on=["market", "product", "uom", "price_vs_control_band"],
    right_on=["market", "product", "uom", "price_vs_control_band"],
    how="inner"
)

results = pd.merge(
    results, dp,
    left_on=["date", "market", "product", "uom", "price_vs_control_band"],
    right_on=["date", "market", "product", "uom", "price_vs_control_band"],
    how="inner"
)

print("\nThe head of results after merging in the results is:\n", results.head(2), "\n")
u = results['product'].unique()
print('The unique products in df are: \n', sorted(u), '\n')
