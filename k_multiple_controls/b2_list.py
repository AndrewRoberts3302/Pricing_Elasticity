import pandas as pd
from a_read_in_the_data import df
from a_read_in_the_data import data_clean
from a_read_in_the_data import data_path

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.width', None)

df.loc[(df['product_group'] == 'Spirits') & (df['uom'] == '25ml'), 'product'] = 'Product Group | Spirits | 25ml'
df.loc[(df['product_group'] == 'LAD') & (df['uom'].isin(['Pint'])), 'product'] = 'Product Group | LAD | Pint'
df.loc[(df['product_group'] == 'Wine') & (df['uom'] == '175ml'), 'product'] = 'Product Group | Wine | 175ml'



def price_banding(df, p=0.2):
    df["price_band"] = ((df["price"] - p) * (1 / p)).astype(int)
    df["price_band"] = (df["price_band"] / (1 / p)) + p

    return df


def get_scenarios(data, products):
    outlets_price = data.groupby(['product', 'price_band']).agg({'outlet': lambda x: set(x)})

    data_int = data[data["product"].isin(products)][["product", "outlet"]]

    data_int = data_int.groupby("product").agg({'outlet': lambda x: set(x)})

    data_int["key"] = 0
    outlets_price["key"] = 0

    data_int = pd.merge(
        left=outlets_price.reset_index(),
        right=data_int.reset_index(),
        on="key", how="outer", suffixes=("_a", "_b")
    )

    data_int = data_int[(data_int["product_a"].isin(products)) * (data_int["product_a"] != data_int["product_b"])]

    data_int["outlet_final"] = list(map(
        lambda x, y:
        set(x & y),
        data_int["outlet_a"],
        data_int["outlet_b"]
    ))

    data_int['scenario'] = list(map(
        lambda x, y, z:
        f'{x} at {y:_.2f} stocked with {z}',
        data_int['product_a'],
        data_int['price_band'],
        data_int['product_b']
    ))

    data_int = data_int[["scenario", "outlet_final", "product_a"]].rename(columns={"product_a": "product"})

    return data_int


def dual_stock(data, products):
    data_int = data[data["product"].isin(products)][["product", "outlet"]]

    data_int = data_int.groupby("product").agg({'outlet': lambda x: set(x)}).reset_index()

    data_int["key"] = 0

    data_int = pd.merge(
        left=data_int,
        right=data_int,
        on="key", how="outer", suffixes=("_a", "_b")
    )

    data_int = data_int[(data_int["product_a"].isin(products)) * (data_int["product_a"] != data_int["product_b"])]

    data_int["outlet_final"] = list(map(
        lambda x, y:
        set(x & y),
        data_int["outlet_a"],
        data_int["outlet_b"]
    ))

    data_int['scenario'] = list(map(
        lambda x, z:
        f'{x} stocked with {z}',
        data_int['product_a'],
        data_int['product_b']
    ))

    data_int = data_int[["scenario", "outlet_final", "product_a"]].rename(columns={"product_a": "product"})

    return data_int


def main():
    df = pd.read_csv(f"{data_path}/{data_clean}", parse_dates=["date"])
    df.loc[(df['product_group'] == 'Spirits') & (df['uom'] == '25ml'), 'product'] = 'Product Group | Spirits | 25ml'
    df.loc[(df['product_group'] == 'LAD') & (df['uom'].isin(['Pint'])), 'product'] = 'Product Group | LAD | Pint'
    df.loc[(df['product_group'] == 'Wine') & (df['uom'] == '175ml'), 'product'] = 'Product Group | Wine | 175ml'



    desired = [
        "Product Group | Spirits | 25ml",
        'Product Group | LAD | Pint',
        "Product Group | Wine | 175ml",
    ]



    df = price_banding(df)

    get_scenarios(data=df, products=desired)



if __name__ == "__main__":
    main()

    print(df.head(200))

