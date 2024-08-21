import pandas as pd
from c_Data_Path.a_data_path import data_path

from j_shares_product_level import product_share
from k_shares_class_level import class_share
from l_shares_group_level import group_share

print("\nThe head of product_share is:\n", product_share.head(2), "\n")
print("\nThe head of class_share is:\n", class_share.head(2), "\n")
print("\nThe head of group_share is:\n", group_share.head(2), "\n")

shares = pd.concat([product_share, class_share, group_share], axis=0)

# Export shares for QC
shares.to_csv(data_path / "qc_shares_vs_index_control.csv", index=False)
