import pandas as pd

from c_rename_the_columns import df, df_data

print("\nThe head of df before merging in the quantity and value data is:\n", df.head(2), "\n")
print("\nThe head of df_data before merging in the quantity and value data is:\n", df_data.head(2), "\n")

df = df.drop(["quantity", "value"], axis=1)

df = pd.merge(
    df, df_data,
    left_on=["outlet", "pm_product_item_id", "uom"],
    right_on=["outlet", "pm_product_item_id", "uom"],
    how="inner"
)
print(df.head(2))