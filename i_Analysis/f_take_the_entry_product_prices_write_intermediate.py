import pandas as pd
from c_Data_Path.a_data_path import data_path

from e_append_products import df

# Take the entry product price

en = df.groupby(
    [
      "date", "outlet", "operator", "market", "product", "product_level", "uom"
        ]
).agg(
    {
        "price": ["min"]
    }
)
en.columns = en.columns.get_level_values(0)
en = en.reset_index()

df = pd.merge(
    df, en,
    left_on=["date", "outlet", "operator", "market", "product", "product_level", "uom", "price"],
    right_on=["date", "outlet", "operator", "market", "product", "product_level", "uom", "price"],
    how="inner"
)

print("\nThe head head of df after obtaining the entry level prices is:\n\n",
      df.head(2))

# Export this data_frame for use in the comparison analysis
df.to_csv(data_path / "intermediate_analysis_df.csv", index=False)
