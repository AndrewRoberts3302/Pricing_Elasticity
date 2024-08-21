import pandas as pd
from pathlib import Path

from x_extract_lists import results, list_markets, list_price_bands, list_products

print("\n-------------------------------------------------------------------\n")
print("RUNNING FILE:", Path(__file__).name)
print("\n-------------------------------------------------------------------\n")

results_all = results.copy()
results_all["sample_size_robustness"] = "All"

results_high = results.loc[results["outlet_count"] >= 50].copy()
results_high["sample_size_robustness"] = "High"

results = pd.concat([results_all, results_high], axis=0)

################################################################################
#EDIT: Remove low sample counts if required for client files.
################################################################################

results = results.loc[(results["sample_size_robustness"] == "High")]

################################################################################


# Reorder
results = results[[
    "date",
    "market",
    "product",
    "price_band",
    "quantity_ros",
    "value_ros",
    "band_quantity_share",
    "band_value_share",
    "outlet_count",
    "dist_pen_share",
    "quantity_ros_vs_avg",
    "quantity_ros_vs_avg_percent",
    "value_ros_vs_avg",
    "value_ros_vs_avg_percent",
    "sample_size_robustness",
    "share_in_class_quantity",
    "share_in_class_value",
    "share_in_group_quantity",
    "share_in_group_value",

    "operator_count",
    "nda_share",
    "nda_operator"

    ]]