from b_review_the_data import df, df_data

print("\nThe column names in the supplied data are:\n", df.columns, "\n")

df = df.rename(
    columns={
        "Rel Week": "rel_week",
        "D_Name": "day_name",
        "D_DateKey": "date",
        "OT_CGAIdent": "outlet",
        "OT_BrandDescription": "outlet_brand",
        "PT_ClassificationLevel6Description": "product_group",
        "PM_ProductItemId": "pm_product_item_id",
        "PM_UomDescription": "uom",
        "PT_GenealogyLevel2Description": "pt_gl2",
        "PT_GenealogyLevel1Description": "product",
        "SumOfSumOfF_SalesQuantity": "quantity",
        "SumOfSumOfF_SalesValue_": "value",
        "Custom Cats": "product_class",
        "RSP": "price",
        "PI_ClientDescription": "data_partner",
        "OT_SL2_CGA": "segment",
        "Price Index": "price_index"
    }
)

df_data = df_data.rename(columns={"pm_uom_description": "uom"})

print("\nThe column names after renaming are:\n", df.columns, "\n")

print(df.head(5))