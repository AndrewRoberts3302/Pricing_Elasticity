from pathlib import Path
from n_apply_ndas import results

print("\n-------------------------------------------------------------------\n")
print("RUNNING FILE:", Path(__file__).name)
print("\n-------------------------------------------------------------------\n")

results = results.copy()
results["uom"] = results["uom"].astype(str)

results["product"] = results["product"] + " | " + results["uom"]

print(results.head(2))

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
    "share_in_class_quantity",
    "share_in_class_value",
    "share_in_group_quantity",
    "share_in_group_value",

    "operator_count",
    "nda_share",
    "nda_operator"
    ]]
