from w_custom_limits_to_results_EDIT_THIS import results

# Extract the markets
list_markets = results["market"].drop_duplicates().sort_values(ascending=True)

# Extract the products
list_products = results["product"].drop_duplicates().sort_values(ascending=True)

# Extract the price bands
list_price_difference_bands = results["price_vs_control_band"].drop_duplicates().sort_values(ascending=True)

#Split the products by the bars.
