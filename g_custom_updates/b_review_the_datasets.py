import pandas as pd

from a_read_in_the_data import(
    df,
    ou_novellus,
    ou_cmbc,
    df_product,
    ou_diageo,
    ou_huk
    # data_product_miller_beer_quality
)

print("\nThe head of the pricing data df is:\n", df.head(2), "\n")
print("\nThe head of the Novellus outlet data is:\n", ou_novellus.head(2), "\n")
print("\nThe head of the CMBC CUK outlet data is:\n", ou_cmbc.head(2), "\n")
print("\nThe head of the product data is:\n", df_product.head(2), "\n")
print("\nThe head of the Diageo outlet data is:\n", ou_diageo.head(2), "\n")
print("\nThe head of the HUK outlet data is: \n\n", ou_huk.head(2))

# Check the outlet counts in the data before merging in any custom data.
n = len(pd.unique(df["outlet"]))
print("\nThe outlet counts in the data before merging in custom outlet data is:", n, "\n")

# Check the row count before applying updates.
print("\nThe shape of the data before applying updates is:\n", df.shape)