import pandas as pd
from functools import reduce
from b2_list import get_scenarios, dual_stock
from a_read_in_the_data import data_path
from a_read_in_the_data import data_clean

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.width', None)

# df.loc[(df['product_group'] == 'Spirits') & (df['uom'] == '25ml'), 'product'] = 'Spirits 25ml'
# df.loc[(df['product_group'] == 'LAD') & (df['uom'].isin(['Pint', 'Half', '568ml'])), 'product'] = 'Draught LAD'
# df.loc[(df['product_group'] == 'Wine') & (df['uom'] == '175ml'), 'product'] = 'Wine 175ml'



def calculate_ros(df):
    ros = df.groupby(
        [
            "market", "product", "uom", "price_band"
        ]
    ).agg(
        {
            "quantity": "sum",
            "value": "sum",
            "outlet": 'nunique',
            "operator": 'nunique'
        }
    )
    ros.columns = ros.columns.get_level_values(0)
    ros = ros.reset_index()

    ros = ros.rename(
        columns={
            "outlet": "outlet_count",
            "operator": "operator_count"
        }
    )

    ros["quantity_ros"] = ros["quantity"] / ros["outlet_count"]
    ros["value_ros"] = ros["value"] / ros["outlet_count"]

    ros = ros[[
        "market", "product", "uom", "price_band", "quantity_ros", "value_ros", "outlet_count", "operator_count"
    ]]

    # Average Ros
    ros_avg = df.groupby(
        [
            "market", "product", "uom", "price_band"
        ]
    ).agg(
        {
            "quantity": ["sum"],
            "value": ["sum"],
            "outlet": pd.Series.nunique,
            "operator": pd.Series.nunique
        }
    )
    ros_avg.columns = ros_avg.columns.get_level_values(0)
    ros_avg = ros_avg.reset_index()

    ros_avg = ros_avg.rename(
        columns={
            "outlet": "total_outlet_count",
            "operator": "operator_count"
        }
    )

    ros_avg["avg_quantity_ros"] = ros_avg["quantity"] / ros_avg["total_outlet_count"]
    ros_avg["avg_value_ros"] = ros_avg["value"] / ros_avg["total_outlet_count"]

    ros_avg = ros_avg.groupby(
        ["market", "product", "uom"]
    ).agg(
        {"avg_quantity_ros": ["mean"],
         "avg_value_ros": ["mean"]
         }
    )
    ros_avg.columns = ros_avg.columns.get_level_values(0)
    ros_avg = ros_avg.reset_index()

    # Total outlet counts
    total_outlet = df.groupby(
        [
            "market", "product", "uom"
        ]
    ).agg(
        {
            "outlet": pd.Series.nunique
        }
    )
    total_outlet.columns = total_outlet.columns.get_level_values(0)
    total_outlet = total_outlet.reset_index()
    total_outlet = total_outlet.rename(columns={"outlet": "total_outlet_count"})

    # Merge the ros results and the ros averages.
    ros = pd.merge(
        ros, ros_avg,
        left_on=["market", "product", "uom"],
        right_on=["market", "product", "uom"],
        how="inner"
    )

    # Merge the total outlet counts.
    ros = pd.merge(
        ros, total_outlet,
        left_on=["market", "product", "uom"],
        right_on=["market", "product", "uom"],
        how="inner"
    )

    # Add in comparison calculations.
    ros["dist_pen_share"] = ros["outlet_count"] / ros["total_outlet_count"]
    ros["quantity_ros_vs_avg"] = ros["quantity_ros"] - ros["avg_quantity_ros"]
    ros["quantity_ros_vs_avg_percent"] = ros["quantity_ros_vs_avg"] / ros["avg_quantity_ros"]
    ros["value_ros_vs_avg"] = ros["value_ros"] - ros["avg_value_ros"]
    ros["value_ros_vs_avg_percent"] = ros["value_ros_vs_avg"] / ros["avg_value_ros"]

    return ros


def product_nda_share(df):
    dp = df.groupby(
        [

            "operator",
            "market",
            "product",
            "uom",
            "price_band"
        ]
    ).agg(
        {
            "volume": ["sum"]
        }
    )
    dp.columns = dp.columns.get_level_values(0)
    dp = dp.reset_index()

    tv = dp.groupby(
        [

            "market",
            "product",
            "uom",
            "price_band"
        ]
    ).agg(
        {
            "volume": ["sum"]
        }
    )
    tv.columns = tv.columns.get_level_values(0)
    tv = tv.reset_index()

    tv = tv.rename(
        columns={
            "volume": "total_volume"
        }
    )

    dp = pd.merge(
        dp, tv,
        left_on=["market", "product", "uom", "price_band"],
        right_on=["market", "product", "uom", "price_band"],
        how="inner"
    )

    dp["dp_share"] = dp["volume"] / dp["total_volume"]

    dp["rank"] = dp.groupby(
        [

            "market",
            "product",
            "uom",
            "price_band"
        ]
    )["dp_share"].rank(ascending=False, method="first")

    dp["rank"] = dp["rank"].astype(int)
    dp = dp.loc[dp["rank"] == 1]

    dp = dp[[

        "market",
        "product",
        "uom",
        "price_band",
        "dp_share",
        "operator"
    ]]

    dp = dp.rename(
        columns={
            "dp_share": "nda_share",
            "operator": "nda_operator"
        }
    )
    return dp


def band_shares(df):
    band_share = df.groupby(
        [
            "market", "product", "uom", "price_band"
        ]
    ).agg(
        {
            "quantity": ["sum"],
            "value": ["sum"]
        }
    )
    band_share.columns = band_share.columns.get_level_values(0)
    band_share = band_share.reset_index()

    # Total values.
    total = band_share.groupby(
        [
            "market", "product", "uom"
        ]
    ).agg(
        {
            "quantity": ["sum"],
            "value": ["sum"]
        }
    )
    total.columns = total.columns.get_level_values(0)
    total = total.reset_index()
    total = total.rename(
        columns={
            "quantity": "total_quantity",
            "value": "total_value"
        }
    )

    # Merge the two dataframes.
    band_share = pd.merge(
        band_share, total,
        left_on=["market", "product", "uom"],
        right_on=["market", "product", "uom"],
        how="inner"
    )

    # Calculate the results.
    band_share["band_quantity_share"] = band_share["quantity"] / band_share["total_quantity"]
    band_share["band_value_share"] = band_share["value"] / band_share["total_value"]

    # Limit the columns.
    band_share = band_share[[
        "market", "product", "uom", "price_band", "band_quantity_share", "band_value_share"
    ]]
    return band_share


def shares_product_level(df):
    df_product = df.copy()

    # Calculate the values for the products
    df_product = df_product.groupby(
        [
            "market", "product", "product_class", "product_group", "uom", "price_band"
        ]
    ).agg(
        {
            "quantity": "sum",
            "value": "sum"
        }
    )

    # Calculate the values for the product classes
    df_product[["class_quantity", "class_value"]] = df_product.groupby(
        [
            "market", "product_class", "uom", "price_band"
        ]
    )[["quantity", "value"]].transform("sum")

    # Calculate the values for the product groups
    df_product[["group_quantity", "group_value"]] = df_product.groupby(
        [
            "market", "product_group", "uom", "price_band"
        ]
    )[["quantity", "value"]].transform("sum")

    df_product["share_in_class_quantity"] = df_product["quantity"] / df_product["class_quantity"]
    df_product["share_in_class_value"] = df_product["value"] / df_product["class_value"]
    df_product["share_in_group_quantity"] = df_product["quantity"] / df_product["group_quantity"]
    df_product["share_in_group_value"] = df_product["value"] / df_product["group_value"]

    product_share = df_product.reset_index()[[
        "market", "product", "uom", "price_band", "share_in_class_quantity", "share_in_class_value",
        "share_in_group_quantity", "share_in_group_value"]]

    return product_share


def shares_class_level(df):
    df_product = df.loc[df["product_level"] == "Product"]

    print("\nThe head of df_product is:\n", df_product.head(2), "\n")

    # Calculate the values for the product classes
    df_product = df_product.groupby(
        [
            "market", "product_class", "product_group", "uom", "price_band"
        ]
    ).agg(
        {
            "quantity": ["sum"],
            "value": ["sum"]
        }
    )
    df_product.columns = df_product.columns.get_level_values(0)
    df_product = df_product.reset_index()
    df_product["product"] = df_product["product_class"]

    # Calculate the values for the product classes
    df_product_class = df_product.groupby(
        [
            "market", "product_class", "uom", "price_band"
        ]
    ).agg(
        {
            "quantity": ["sum"],
            "value": ["sum"]
        }
    )
    df_product_class.columns = df_product_class.columns.get_level_values(0)
    df_product_class = df_product_class.reset_index()
    df_product_class = df_product_class.rename(columns={
        "quantity": "class_quantity",
        "value": "class_value"})

    # Calculate the values for the product classes
    df_product_group = df_product.groupby(
        [
            "market", "product_group", "uom", "price_band"
        ]
    ).agg(
        {
            "quantity": ["sum"],
            "value": ["sum"]
        }
    )
    df_product_group.columns = df_product_group.columns.get_level_values(0)
    df_product_group = df_product_group.reset_index()
    df_product_group = df_product_group.rename(columns={
        "quantity": "group_quantity",
        "value": "group_value"})

    # Merge the results
    df_product = pd.merge(
        df_product, df_product_class,
        left_on=["market", "product_class", "uom", "price_band"],
        right_on=["market", "product_class", "uom", "price_band"],
        how="inner"
    )

    df_product = pd.merge(
        df_product, df_product_group,
        left_on=["market", "product_group", "uom", "price_band"],
        right_on=["market", "product_group", "uom", "price_band"],
        how="inner"
    )

    df_product["share_in_class_quantity"] = df_product["quantity"] / df_product["class_quantity"]
    df_product["share_in_class_value"] = df_product["value"] / df_product["class_value"]
    df_product["share_in_group_quantity"] = df_product["quantity"] / df_product["group_quantity"]
    df_product["share_in_group_value"] = df_product["value"] / df_product["group_value"]

    class_share = df_product[[
        "market", "product", "uom", "price_band", "share_in_class_quantity", "share_in_class_value",
        "share_in_group_quantity", "share_in_group_value"]].copy()
    class_share["product"] = "Product Class | " + class_share["product"]

    print(class_share.head(2))
    return class_share


def shares_group_level(df):
    df_product = df.loc[df["product_level"] == "Product"]

    print("\nThe head of df_product is:\n", df_product.head(2), "\n")

    # Calculate the values for the product classes
    df_product = df_product.groupby(
        [
            "market", "product_group", "uom", "price_band"
        ]
    ).agg(
        {
            "quantity": ["sum"],
            "value": ["sum"]
        }
    )
    df_product.columns = df_product.columns.get_level_values(0)
    df_product = df_product.reset_index()
    df_product["product"] = df_product["product_group"]
    df_product["product_class"] = df_product["product_group"]

    # Calculate the values for the product classes
    df_product_class = df_product.groupby(
        [
            "market", "product_class", "uom", "price_band"
        ]
    ).agg(
        {
            "quantity": ["sum"],
            "value": ["sum"]
        }
    )
    df_product_class.columns = df_product_class.columns.get_level_values(0)
    df_product_class = df_product_class.reset_index()
    df_product_class = df_product_class.rename(columns={
        "quantity": "class_quantity",
        "value": "class_value"})

    # Calculate the values for the product classes
    df_product_group = df_product.groupby(
        [
            "market", "product_group", "uom", "price_band"
        ]
    ).agg(
        {
            "quantity": ["sum"],
            "value": ["sum"]
        }
    )
    df_product_group.columns = df_product_group.columns.get_level_values(0)
    df_product_group = df_product_group.reset_index()
    df_product_group = df_product_group.rename(columns={
        "quantity": "group_quantity",
        "value": "group_value"})

    # Merge the results
    df_product = pd.merge(
        df_product, df_product_class,
        left_on=["market", "product_class", "uom", "price_band"],
        right_on=["market", "product_class", "uom", "price_band"],
        how="inner"
    )

    df_product = pd.merge(
        df_product, df_product_group,
        left_on=["market", "product_group", "uom", "price_band"],
        right_on=["market", "product_group", "uom", "price_band"],
        how="inner"
    )

    df_product["share_in_class_quantity"] = df_product["quantity"] / df_product["class_quantity"]
    df_product["share_in_class_value"] = df_product["value"] / df_product["class_value"]
    df_product["share_in_group_quantity"] = df_product["quantity"] / df_product["group_quantity"]
    df_product["share_in_group_value"] = df_product["value"] / df_product["group_value"]

    group_share = df_product[[
        "market", "product", "uom", "price_band", "share_in_class_quantity", "share_in_class_value",
        "share_in_group_quantity", "share_in_group_value"]].copy()
    group_share["product"] = "Product Group | " + group_share["product"]

    print(group_share.head(2))
    return group_share


def get_results(df, scenario, outlets, product):
    cactus = df[df["outlet"].isin(outlets)]
    output = reduce(
        lambda left, right:
        pd.merge(
            left=left, right=right, how="inner", on=["market", "product", "uom", "price_band"]
        ), [
            calculate_ros(cactus),
            product_nda_share(cactus),
            band_shares(cactus),
            shares_product_level(cactus)
        ]
    )
    output["scenario"] = scenario
    output = output[output["product"].isin([product])]
    return output


def price_banding(df, p=0.2):
    df["price_band"] = ((df["price"] - p) * (1 / p)).astype(int)
    df["price_band"] = (df["price_band"] / (1 / p)) + p

    return df


def append_markets(df):
    def create_market_break(market_break, string_modifier):
        data_new = df[[
            "outlet", "operator", "product", "product_class", "product_group", "uom", "quantity",
            "value", "volume", "price", 'price_band'
        ] + [market_break]].rename(columns={market_break: "market"})

        data_new["market"] = data_new['market'].apply(lambda x: f"{string_modifier} | {x}")

        return data_new

    df["country"] = "GB"

    breaks = {
        'country': 'Country',
        'region': 'Region',
        'is_london': 'London',
        'segment': 'Segment',
        'quality': 'Quality'
        # ,
        # 'south_and_south_west': 'South and South West'
    }

    data_out = pd.concat([
        create_market_break(key, value) for key, value in breaks.items()
    ])

    return data_out


def main():
    data = pd.read_csv(f"{data_path}/{data_clean}", parse_dates=["date"])
    data.loc[(data['product_group'] == 'Spirits') & (data['uom'] == '25ml'), 'product'] = 'Product Group | Spirits | 25ml'
    data.loc[(data['product_group'] == 'LAD') & (data['uom'].isin(['Pint'])), 'product'] = 'Product Group | LAD | Pint'
    data.loc[(data['product_group'] == 'Wine') & (data['uom'] == '175ml'), 'product'] = 'Product Group | Wine | 175ml'

    desired = [
        "Product Group | Spirits | 25ml",
        'Product Group | LAD | Pint',
        "Product Group | Wine | 175ml",
    ]

    data = price_banding(data)

    # scenarios = pd.concat([
    #     get_scenarios(data=data, products=beers),
    #     get_scenarios(data=data, products=ciders)
    # ])

    scenarios = pd.concat([
        dual_stock(data=data, products=desired),
    ])

    data = append_markets(df=data)

    output = pd.concat([
        get_results(df=data, scenario=row["scenario"], outlets=row["outlet_final"], product=row["product"])
        for _, row in scenarios.iterrows()
    ])
    print(output.head())

    output.to_csv("result_final_dual_stock.csv", index=False)


if __name__ == "__main__":
    main()
