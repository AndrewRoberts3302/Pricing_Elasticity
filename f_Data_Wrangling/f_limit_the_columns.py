from e_remove_certain_prices import df

# Limit the columns.
###############################################
#project 850
allowed_classes_spirits = ['Gin', 'Flavoured Vodka', 'Non Flavoured Vodka', 'Dark Rum', 'Golden Rum', 'White Rum']
df = df[(df['product_group'] != 'Spirits') | (df['product_class'].isin(allowed_classes_spirits))]

allowed_classes_wine = ['Rose Wine', 'White Wine', 'Red Wine']
df = df[(df['product_group'] != 'Wine/Champagne') | (df['product_class'].isin(allowed_classes_wine))]

df['product_group'] = df['product_group'].replace('Wine/Champagne', 'Wine')

##################################################################################

df = df[[
    "date",
    "outlet",
    "operator",
    "outlet_brand",
    "data_partner",
    "pm_product_item_id",
    "product",
    "product_class",
    "product_group",
    "uom",
    "price",
    "quantity",
    "value",
    "volume"
    ]]

