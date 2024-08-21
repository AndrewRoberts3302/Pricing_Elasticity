from a_read_in_the_clean_data import df

df = df[~df["product"].str.contains("All Other")]
df = df[~df["product"].str.contains("Any Other")]
df = df[~df["product"].str.contains("nknown")] # To get rid of items that would be Unknown or unknown
