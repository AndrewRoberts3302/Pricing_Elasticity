"""
Comment the script out if the aggregation is not required.
Note that this updates from Novellus level 2.
"""

import numpy as np

from i_aggregate_outlet_qualities_OPTION import (
    df,
    df_product
    # data_product_miller_beer_quality
)

###############################################################################
# Update outlet segments from Novellus level 2.

# u = df["segment"].unique()
# print("\nThe segments are:\n\n", sorted(u))
#
# # Bars
# df.loc[df["segment"].isin([
#     "Large Venue",
#     "Nightclub",
#     "Hotel",
#     "Guest/Boarding House",
#     "Bar"
#     ]
# ), "segment"] = "Bars"
#
# # Pubs
# df.loc[df["segment"].isin([
#     "Holiday/Caravan Park",
#     "Sports/Social Club",
#     "Community Pub",
#     "Food Pub",
#     "High Street Pub"
#     ]
# ), "segment"] = "Pubs"
#
# # Restaurants
# df.loc[df["segment"].isin([
#     "Bar Restaurant",
#     "Cafe/Delicatessen",
#     "Restaurant",
#     "Casual Dining Restaurant"
#     ]
# ), "segment"] = "Restaurants"
#
# u = df["segment"].unique()
# print("\nThe segments are now:\n\n", sorted(u))
###############################################################################
