from c_review_the_data import df

df["uom"] = df["uom"].astype(str)
df["product"] = df["product"] + " | " + df["uom"]