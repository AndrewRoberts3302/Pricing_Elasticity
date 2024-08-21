import pandas as pd

from h_1_product_ros import df

# Calculate the shares of the price bands.

# Band values.
band_share = df.groupby(
    [
        "date", "market", "product", "uom", "price_vs_control_band"
        ]
).agg(
    {
        "quantity": ["sum"],
        "value": ["sum"]
    }
)
band_share.columns = band_share.columns.get_level_values(0)
band_share = band_share.reset_index()

# Total values.
total = band_share.groupby(
    [
        "date", "market", "product", "uom"
        ]
).agg(
    {
        "quantity": ["sum"],
        "value": ["sum"]
    }
)
total.columns = total.columns.get_level_values(0)
total = total.reset_index()
total = total.rename(
    columns={
        "quantity": "total_quantity",
        "value": "total_value"
    }
)

# Merge the two dataframes.
band_share = pd.merge(
    band_share, total,
    left_on=["date", "market", "product", "uom"],
    right_on=["date", "market", "product", "uom"],
    how="inner"
)

# Calculate the results.
band_share["band_quantity_share"] = band_share["quantity"] / band_share["total_quantity"]
band_share["band_value_share"] = band_share["value"] / band_share["total_value"]

# Limit the columns.
band_share = band_share[[
    "date", "market", "product", "uom", "price_vs_control_band", "band_quantity_share", "band_value_share"
    ]]
