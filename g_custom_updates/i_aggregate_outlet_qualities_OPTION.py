import numpy as np

from h_apply_custom_CMBC_CUK_product_data_OPTION import (
    df,
    df_product
    # data_product_miller_beer_quality
)

###############################################################################
# Update outlet quality.
# df.loc[df["quality"].isin(["Gold", "Platinum"]), "quality"] = "Premium"
# df.loc[df["quality"].isin(["Bronze", "Silver"]), "quality"] = "Mainstream"
###############################################################################

# Check the row count after updating the outlet qualities.
print(
    "\nThe shape of the data before after after updating the outlet qualities "
    "is:\n", df.shape
)