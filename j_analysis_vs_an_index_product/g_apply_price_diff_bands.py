from f_split_control_and_re_merge import df

###############################################################################
# Set the price band differences.
# p = 0.5  # 50p price bands from the lowest value rounded down to the nearest pound.
p = 0.2  # 20p price bands from the lowest value rounded down to the nearest pound.
###############################################################################

print("\nThe head of df before applying price difference bands is:\n", df.head(2), "\n")

min_price_diff = df["price_vs_control"].min()
max_price_diff = df["price_vs_control"].max()

print("\nThe miniumum price difference vs the control product is:", min_price_diff, "\n")
print("\nThe maxiumum price difference vs the control product is:", max_price_diff, "\n")

# Assign the price band based on p.
df["price_band_control"] = ((df["control_price"] - p) * (1 / p)).astype(int)
df["price_band_control"] = (df["price_band_control"] / (1 / p)) + p

df["price_vs_control_band"] = df["price_band"] - df["price_band_control"]

# Round price_vs_control_band column to 1 dp

decimals = 1
df['price_vs_control_band'] = df['price_vs_control_band'].apply(lambda x: round(x, decimals))

print("\nThe head of df after applying price difference bands is:\n", df.head(2), "\n")