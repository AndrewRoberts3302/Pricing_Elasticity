import pandas as pd
from pathlib import Path

from w_custom_limits_to_results_EDIT_THIS import results
from e_append_products import list_products

print("\n-------------------------------------------------------------------\n")
print("RUNNING FILE:", Path(__file__).name)
print("\n-------------------------------------------------------------------\n")

# Extract the products
list_products_results = results["product"].drop_duplicates().sort_values(ascending=True)
list_products = pd.merge(
    list_products, list_products_results,
    left_on=["product"], right_on=["product"],
    how="inner"
)
list_products = list_products.sort_values(
    by=["product"],
    ascending=[True]
)

# Extract the markets
list_markets = results["market"].drop_duplicates().sort_values(ascending=True)

# Extract the price bands
list_price_bands = results["price_band"].drop_duplicates().sort_values(ascending=True)
