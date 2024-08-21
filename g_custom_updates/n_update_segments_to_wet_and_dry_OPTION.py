from pathlib import Path
import numpy as np

from m_update_regions_to_north_and_south_OPTION import df

print("\n-------------------------------------------------------------------\n")
print("RUNNING FILE: ", Path(__file__).name)
print("\n-------------------------------------------------------------------\n")

# print("\nThe head of df is:\n\n", df.head(2))
#
# u = df["segment"].unique()
#
# print("\nThe unique segments currently are:\n\n", sorted(u))
#
# conditions = [
#     (df["segment"] == "Bar"),
#     (df["segment"] == "Bar Restaurant"),
#     (df["segment"] == "Casual Dining Restaurant"),
#     (df["segment"] == "Community Pub"),
#     (df["segment"] == "Food Pub"),
#     (df["segment"] == "Guest/Boarding House"),
#     (df["segment"] == "High Street Pub"),
#     (df["segment"] == "Holiday/Caravan Park"),
#     (df["segment"] == "Hotel"),
#     (df["segment"] == "Large Venue"),
#     (df["segment"] == "Nightclub"),
#     (df["segment"] == "Restaurant"),
#     (df["segment"] == "Sports/Social Club")
#     ]
# choices = [
#     "Wet Led",
#     "Dry Led",
#     "Dry Led",
#     "Wet Led",
#     "Dry Led",
#     "Not Applicable",
#     "Wet Led",
#     "Not Applicable",
#     "Dry Led",
#     "Wet Led",
#     "Wet Led",
#     "Dry Led",
#     "Wet Led"
# ]
# df["segment"] = np.select(conditions, choices)
#
# u = df["segment"].unique()
# print("\nThe unique segments in df are now:\n\n", sorted(u))
#
# df = df.loc[df["segment"] != "Not Applicable"]