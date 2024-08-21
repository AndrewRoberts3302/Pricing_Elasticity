"""
Comment out this script if this update is not required.
"""

import numpy as np

from e_apply_custom_CMBC_CUK_outlet_segments_OPTION import (
    df,
    df_product,
    ou_diageo,
    ou_huk
    # data_product_miller_beer_quality
)
################################################################################
# Update the Diageo segments.

# u = df['segment'].unique()
# print('The unique segments in df before updating are: \n', sorted(u), '\n')
#
# conditions = [
#     (df["segment"] == "Bar"),
#     (df["segment"] == "Bar Restaurant"),
#     (df["segment"] == "Casual Dining Restaurant"),
#     (df["segment"] == "Community Pub"),
#     (df["segment"] == "Food Pub"),
#     (df["segment"] == "High Street Pub"),
#     (df["segment"] == "Hotel"),
#     (df["segment"] == "Large Venue"),
#     (df["segment"] == "Nightclub"),
#     (df["segment"] == "Restaurant"),
#     (df["segment"] == "Sports / Social Club")
# ]
# choices = [
#     "Cocktail Bar",
#     "Cocktail Bar",
#     "Casual Dining",
#     "Wet Pub",
#     "Food Pub",
#     "Wet Pub",
#     "Hotels",
#     "Enertainment/Venues (Permanent)",
#     "Nightclub",
#     "Restaurant",
#     "Sports and Social"
#     ]
# df["segment"] = np.select(conditions, choices)
#
# df["segment"] = df["segment"].replace("0", "Unclassified Segment")
