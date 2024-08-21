"""
Review the outlet counts after any custom outlet updates
"""

import pandas as pd

from f2_update_with_huk_outlet_segments_OPTION import (
    df,
    df_product
    # data_product_miller_beer_quality
)

n = len(pd.unique(df["outlet"]))
print(
    "\nThe outlet counts in the data after merging in any custom outlet data \
is:", n, "\n"
)
