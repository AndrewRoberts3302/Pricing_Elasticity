import pandas as pd

from b_review_the_datasets import (
    df,
    ou_novellus,
    ou_cmbc,
    df_product,
    ou_diageo,
    ou_huk
    # data_product_miller_beer_quality
)

######################################################################################################################
# Merge in novellus segment, region and quality.

df = pd.merge(
    df, ou_novellus,
    left_on=["outlet"],
    right_on=["outlet"],
    how="inner"
)

# Check the row count after adding in novelus segments and regions.
print(
    "\nThe shape of the data before after applying Novellus segments, "
    "regions and quality is:\n", df.shape
)
######################################################################################################################
