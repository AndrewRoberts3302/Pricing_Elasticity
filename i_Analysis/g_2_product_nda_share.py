from pathlib import Path
import pandas as pd
from c_Data_Path.a_data_path import data_path

from g_1_product_ros import df, ros

print("\n-------------------------------------------------------------------\n")
print("RUNNING FILE: ", Path(__file__).name)
print("\n-------------------------------------------------------------------\n")

print("\nThe head of df is:\n\n", df.head(2))

print("\nThe results for this will need to merge on to the ros results.\n")
print("\nThe head of ros is:\n\n", ros.head(2))

dp = df.groupby(
    [
        "date",
        "operator",
        "market",
        "product",
        "uom",
        "price_band"
        ]
).agg(
    {
        "volume": ["sum"]
    }
)
dp.columns = dp.columns.get_level_values(0)
dp = dp.reset_index()

tv = dp.groupby(
    [
        "date",
        "market",
        "product",
        "uom",
        "price_band"
        ]
).agg(
    {
        "volume": ["sum"]
    }
)
tv.columns = tv.columns.get_level_values(0)
tv = tv.reset_index()

tv = tv.rename(
    columns={
        "volume": "total_volume"
    }
)

print("\nThe head of dp is:\n\n", dp.head(2))
print("\nThe head of tv is:\n\n", tv.head(2))

dp = pd.merge(
    dp, tv,
    left_on=["date", "market", "product", "uom", "price_band"],
    right_on=["date", "market", "product", "uom", "price_band"],
    how="inner"
)

dp["dp_share"] = dp["volume"] / dp["total_volume"]

dp["rank"] = dp.groupby(
    [
        "date",
        "market",
        "product",
        "uom",
        "price_band"
        ]
)["dp_share"].rank(ascending=False, method="first")

dp["rank"] = dp["rank"].astype(int)
dp = dp.loc[dp["rank"] == 1]

dp = dp[[
    "date",
    "market",
    "product",
    "uom",
    "price_band",
    "dp_share",
    "operator"
    ]]

dp = dp.rename(
    columns={
        "dp_share": "nda_share",
        "operator": "nda_operator"
    }
)
