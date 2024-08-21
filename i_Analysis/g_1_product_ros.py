from pathlib import Path
import pandas as pd
from c_Data_Path.a_data_path import data_path

from f_take_the_entry_product_prices_write_intermediate import df

print("\n-------------------------------------------------------------------\n")
print("RUNNING FILE: ", Path(__file__).name)
print("\n-------------------------------------------------------------------\n")

print("\nThe head of df is:\n\n", df.head(2))

# Check the outlet counts in the data before the ros.
n = len(pd.unique(df["outlet"]))
print("\nThe outlet counts in the data before Ros is:", n, "\n")

# Ros results
ros = df.groupby(
    [
        "date", "market", "product", "uom", "price_band"
        ]
).agg(
    {
        "quantity": ["sum"],
        "value": ["sum"],
        "outlet": pd.Series.nunique,
        "operator": pd.Series.nunique
    }
)
ros.columns = ros.columns.get_level_values(0)
ros = ros.reset_index()

ros = ros.rename(
    columns={
        "outlet": "outlet_count",
        "operator": "operator_count"
    }
)

ros["quantity_ros"] = ros["quantity"] / ros["outlet_count"]
ros["value_ros"] = ros["value"] / ros["outlet_count"]

ros = ros[[
    "date", "market", "product", "uom", "price_band", "quantity_ros", "value_ros", "outlet_count", "operator_count"
    ]]

# Average Ros
ros_avg = df.groupby(
    [
        "date", "market", "product", "uom", "price_band"
        ]
).agg(
    {
        "quantity": ["sum"],
        "value": ["sum"],
        "outlet": pd.Series.nunique,
        "operator": pd.Series.nunique
    }
)
ros_avg.columns = ros_avg.columns.get_level_values(0)
ros_avg = ros_avg.reset_index()

ros_avg = ros_avg.rename(
    columns={
        "outlet": "total_outlet_count",
        "operator": "operator_count"
    }
)

ros_avg["avg_quantity_ros"] = ros_avg["quantity"] / ros_avg["total_outlet_count"]
ros_avg["avg_value_ros"] = ros_avg["value"] / ros_avg["total_outlet_count"]

ros_avg = ros_avg.groupby(
    ["date", "market", "product", "uom"]
).agg(
    {"avg_quantity_ros": ["mean"],
     "avg_value_ros": ["mean"]
     }
)
ros_avg.columns = ros_avg.columns.get_level_values(0)
ros_avg = ros_avg.reset_index()

# Total outlet counts
total_outlet = df.groupby(
    [
        "date", "market", "product", "uom"
        ]
).agg(
    {
        "outlet": pd.Series.nunique
    }
)
total_outlet.columns = total_outlet.columns.get_level_values(0)
total_outlet = total_outlet.reset_index()
total_outlet = total_outlet.rename(columns={"outlet": "total_outlet_count"})

# Merge the ros results and the ros averages.
ros = pd.merge(
    ros, ros_avg,
    left_on=["date", "market", "product", "uom"],
    right_on=["date", "market", "product", "uom"],
    how="inner"
)

# Merge the total outlet counts.
ros = pd.merge(
    ros, total_outlet,
    left_on=["date", "market", "product", "uom"],
    right_on=["date", "market", "product", "uom"],
    how="inner"
)

# Add in comparison calculations.
ros["dist_pen_share"] = ros["outlet_count"] / ros["total_outlet_count"]
ros["quantity_ros_vs_avg"] = ros["quantity_ros"] - ros["avg_quantity_ros"]
ros["quantity_ros_vs_avg_percent"] = ros["quantity_ros_vs_avg"] / ros["avg_quantity_ros"]
ros["value_ros_vs_avg"] = ros["value_ros"] - ros["avg_value_ros"]
ros["value_ros_vs_avg_percent"] = ros["value_ros_vs_avg"] / ros["avg_value_ros"]

print("\nThe head of ros is:\n\n", ros.head(2))
# Export Ros for QC
ros.to_csv(data_path / "qc_ros.csv", index=False)
