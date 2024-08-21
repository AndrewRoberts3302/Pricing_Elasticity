"""
Comment out the script if the aggregation is not required.
"""

import numpy as np

from j_aggregate_outlet_segments_OPTION import (
    df,
    df_product
    # data_product_miller_beer_quality
)

###############################################################################
# Update the regions from Novellus level 2.
u = df["region"].unique()
print("\nThe unique regions in the data are:\n", sorted(u), "\n")

# Assign regions.
conditions = [
    (df["region"] == "Central"),
    (df["region"] == "East"),
    (df["region"] == "Lancashire"),
    (df["region"] == "London"),
    (df["region"] == "North East"),
    (df["region"] == "Scotland"),
    (df["region"] == "South & South East"),
    (df["region"] == "South West"),
    (df["region"] == "Wales"),
    (df["region"] == "Yorkshire")
    ]
choices = [
    "Central / Wales",
    "Central / Wales",
    "North",
    "London",
    "North",
    "Scotland",
    "South",
    "South",
    "Central / Wales",
    "North"
    ]
df["region"] = np.select(conditions, choices)

# Check the updated regions.
u = df["region"].unique()
print("\nThe unique regions in the data are now reassigned as:\n", sorted(u), "\n")
###############################################################################