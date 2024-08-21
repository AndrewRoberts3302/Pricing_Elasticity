import pandas as pd

from c_apply_price_bands_EDIT_THIS import df

# Country
df["country"] = "GB"

country = df[[
    "date", "outlet", "operator", "country", "product", "product_class", "product_group", "uom", "quantity", "value", "volume", "price", "price_band"
    ]]
country = country.rename(columns={"country": "market"})
country["market"] = "Country | " + country["market"]

# Region
region = df[[
    "date", "outlet", "operator", "region", "product", "product_class", "product_group", "uom", "quantity", "value", "volume", "price", "price_band"
    ]]
region = region.rename(columns={"region": "market"})
region["market"] = "Region | " + region["market"]

# London or Excluding London
london = df[[
    "date", "outlet", "operator", "is_london", "product", "product_class", "product_group", "uom", "quantity", "value", "volume", "price", "price_band"
    ]]
london = london.rename(columns={"is_london": "market"})
london["market"] = "London | " + london["market"]

# Segment
segment = df[[
    "date", "outlet", "operator", "segment", "product", "product_class", "product_group", "uom", "quantity", "value", "volume", "price", "price_band"
    ]]
segment = segment.rename(columns={"segment": "market"})
segment["market"] = "Segment | " + segment["market"]

# Quality
quality = df[[
    "date", "outlet", "operator", "quality", "product", "product_class", "product_group", "uom", "quantity", "value", "volume", "price", "price_band"
    ]]
quality = quality.rename(columns={"quality": "market"})
quality["market"] = "Quality | " + quality["market"]

# Append the dataframes
df = pd.concat([country, region, london, segment, quality])
