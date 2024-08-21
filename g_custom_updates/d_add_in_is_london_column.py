import numpy as np
from c_merge_in_novellus_and_outlet_quality_data import (
    df,
    ou_cmbc,
    df_product,
    ou_diageo,
    ou_huk
    # data_product_miller_beer_quality
)

conditions = [
    (df["region"] == "London"),
    (df["region"] != "London")
    ]
choices = [
    "London", "Excluding London"
    ]
df["is_london"] = np.select(conditions, choices)

# Check the row count after adding in the London column.
print(
    "\nThe shape of the data before after adding the is_london column is:\n",
    df.shape
)

