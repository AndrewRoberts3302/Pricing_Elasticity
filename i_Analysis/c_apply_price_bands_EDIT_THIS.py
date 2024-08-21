from b_review_the_data import df

###############################################################################
# Set the price band differences.
# p = 0.5  # 50p price bands from the lowest value rounded down to the nearest pound.
p = 0.2  # 20p price bands from the lowest value rounded down to the nearest pound.
###############################################################################

# Identify the minimum price in the data.

min_price = df["price"].min()
max_price = df["price"].max()

print("\nThe minimum price in the data is:", min_price, "\n")
print("\nThe maximum price in the data is:", max_price, "\n")

# Add in a band that starts at the min_price rounded down to the nearest pound.
# Bands go up in the parameters price as set.

# Round down the lowest price to the nearerst pound / integer.
x = min_price.astype(int)

# Assign the price band based on p.
df["price_band"] = ((df["price"] - p) * (1 / p)).astype(int)
df["price_band"] = (df["price_band"] / (1 / p)) + p

# For example:
# with p = 0.2 which is 20p.
# a price of 5.05p would be represented as 5.00
# a price of 5.19 would be represented as 5.0
# a price of 5.20 would be represented as 5.2 which is 5 pound and 20p.