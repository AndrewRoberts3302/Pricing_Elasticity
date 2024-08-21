import pandas as pd
import numpy as np

# export the dataframes to qc why they are not merging correctly

from pathlib import Path
cwd = Path(__file__).parent

from b_remove_bad_values import df

print("\nThe head of the clean data is:\n", df.head(2), "\n")

# Check the shape of the data before removing outliers.
print("\nThe shape of df before removing outliers based on product price is:\n", df.shape, "\n")

# Remove outliers based on product price

# Aggregate the columns required.
# Note that no aggregation is required for pricing but the columns do need limiting to those used in removing outliers.

ag = df[[
        "date",
        "outlet",
        "operator",
        "segment",
        "region",
        "quality",
        "product",
        "uom",
        "price"
        ]]
# Mean and standard deviations.

msd = ag.groupby(
    [
        "date",
        "segment",
        "region",
        "quality",
        "product",
        "uom"
        ]
).agg(
    {
        "price": ["mean", np.std],
        "outlet": pd.Series.nunique
    }
)
msd.columns = msd.columns.map("|".join).str.strip("|")
msd = msd.reset_index()
msd = msd.rename(
    columns={
        "outlet|nunique": "outlet|count"
    }
)

# Results with one outlet won't have standard deviations, remove those.
msd = msd.loc[msd["outlet|count"] > 1]

# Merge and calculate z-scores

z = pd.merge(
    ag, msd,
    left_on=[
        "date",
        "segment",
        "region",
        "quality",
        "product",
        "uom",
        ],
    right_on=[
        "date",
        "segment",
        "region",
        "quality",
        "product",
        "uom",
        ],
    how="inner"
)

z["z_score"] = (z["price"] - z["price|mean"]) / z["price|std"]
z["z_score"] = z["z_score"].abs()

# Take the acceptable rows.
z = z.loc[z["z_score"] < 2]

print(z.head(2))
print(df.head(2))
# Take the columns required for merging.
z = z[[
    "date",
    "outlet",
    "segment",
    "region",
    "quality",
    "product",
    "uom",
    "price"
    ]]

# Merge the acceptable rows with the data.
df = pd.merge(
    df, z,
    left_on=[
        "date",
        "outlet",
        "segment",
        "region",
        "quality",
        "product",
        "uom",
        "price"
        ],
    right_on=[
        "date",
        "outlet",
        "segment",
        "region",
        "quality",
        "product",
        "uom",
        "price"
        ],
    how="inner"
)

# Check the shape of the data after removing outliers.
print("\nThe shape of df after removing outliers based on product price is:\n", df.shape, "\n")

print("\nThe head of df after removing outliers based on product price is:\n\n", df.head(2))

