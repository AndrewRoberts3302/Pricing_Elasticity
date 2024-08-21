from pathlib import Path
from c_Data_Path.a_data_path import data_path

from y_append_results_copy_with_high_outlet_counts_OPTION import results, list_markets, list_price_bands, list_products

print("\n-------------------------------------------------------------------\n")
print("RUNNING FILE:", Path(__file__).name)
print("\n-------------------------------------------------------------------\n")

# cwd = Path(__file__).parent

results.to_csv(data_path / "results.csv", index=False)
list_products.to_csv(data_path / "list_products.csv", index=False)
list_markets.to_csv(data_path / "list_markets.csv", index=False)
list_price_bands.to_csv(data_path / "list_price_bands.csv", index=False)
