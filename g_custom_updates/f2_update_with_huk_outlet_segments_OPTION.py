from pathlib import Path
import pandas as pd

from f1_apply_custom_diageo_segments_OPTION import (
    df,
    df_product,
    ou_diageo,
    ou_huk
    # data_product_miller_beer_quality
)

print("\n-------------------------------------------------------------------\n")
print(Path(__file__).name)
print("\n-------------------------------------------------------------------\n")

print("\nThe head of df is: \n\n", df.head(2))
print("\nThe head of huk segment data ou_huk is: \n\n", ou_huk.head(2))

# Comment out if not required.

# df = df.drop(
#     [
#         "segment"
#         ], axis=1
# )
#
# df = pd.merge(
#     df, ou_huk,
#     left_on=["outlet"],
#     right_on=["outlet"]
# )
