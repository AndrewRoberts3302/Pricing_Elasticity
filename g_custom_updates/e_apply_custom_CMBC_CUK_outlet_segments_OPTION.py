"""
Comment out the script if this update is not required.
"""

import pandas as pd

from d_add_in_is_london_column import (
    df,
    ou_cmbc,
    df_product,
    ou_diageo,
    ou_huk
    # data_product_miller_beer_quality
)

######################################################################################################################
# Merge in CMBC / CUK segment.
# Comment out if not required.

# First you need to merge in the Novellus data.

# Then merge in the CMBC / CUK outlet data
# df = pd.merge(
#     df, ou_cmbc,
#     left_on=["segment", "quality"],
#     right_on=["ot_sl2_novellus", "ot_quality_model"],
#     how="inner"
# )
#
# # Drop the columns.
# df = df.drop(["segment", "ot_quality_model", "ot_sl2_novellus"], axis=1)
#
# # Rename the segment column.
# df = df.rename(columns={"cuk_segmentation": "segment"})

######################################################################################################################
