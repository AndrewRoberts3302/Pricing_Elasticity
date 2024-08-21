import pandas as pd


from d_append_markets import df

# Check the columns available for appending.
print("\nThe columns in df are:", df.columns)

# Check for NaN values in the product column.
print('Checking if there are any nulls in the product column before appending product: ',
      df['product'].isnull().values.any(), '\n')

# Check for NaN values in the product class column.
print('Checking if there are any nulls in the product class column before appending product: ',
      df['product_class'].isnull().values.any(), '\n')

# Check for NaN values in the product group column.
print('Checking if there are any nulls in the product group column before appending product: ',
      df['product_group'].isnull().values.any(), '\n')

# Take the various product columns.

product = df[[
    "date", "outlet", "operator", "market", "product", "product_class", "product_group", "uom", "quantity", "value",  "volume", "price", "price_band"
    ]].copy()
product["product"] = "Product | " + product["product"]
product["product_level"] = "Product"

product_class = df[[
    "date", "outlet", "operator", "market", "product_class", "product_group", "uom", "quantity", "value",  "volume", "price", "price_band"
    ]].copy()
product_class["product"] = "Product Class | " + product_class["product_class"]
product_class["product_level"] = "Product Class"

product_group = df[[
    "date", "outlet", "operator", "market", "product_group", "uom", "quantity", "value",  "volume", "price", "price_band"
    ]].copy()
product_group["product_class"] = "NA Product Group"
product_group["product"] = "Product Group | " + product_group["product_group"]
product_group["product_level"] = "Product Group"

#Check the heads of the dataframes before appending them.
print("\nThe head of dataframe product before appending all products is:\n", product.head(2), "\n")
print("\nThe head of dataframe product_class before appending all products is:\n", product_class.head(2), "\n")
print("\nThe head of dataframe product_group before appending all products is:\n", product_group.head(2), "\n")

df = pd.concat([product, product_class, product_group], axis=0)

# Check for NaN values in the product column.
print('Checking if there are any nulls in the product column after appending product: ',
      df['product'].isnull().values.any(), '\n')

print("\nThe head of df after appending products is:\n\n", df.head(2))

# Take the product, class and group to use later when creating the product list.
list_products = df[["product", "uom", "product_class", "product_group"]].copy()
list_products["product"] = list_products["product"] + " | " + list_products["uom"]
list_products = list_products.drop(["uom"], axis=1)
list_products = list_products.drop_duplicates()
