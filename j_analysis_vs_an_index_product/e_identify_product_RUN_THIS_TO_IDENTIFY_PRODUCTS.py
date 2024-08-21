import numpy as np

from d_concat_product_and_uom import df
from a_parameters_EDIT_THIS import control_product

control_product_string = control_product[0]
control_product = control_product_string

# Find the Control Products in the data.
p = df[["product"]]
p = p[p["product"].str.contains(control_product)]
p = p.drop_duplicates()
print("\nProducts in the data containing the control product name are:\n", p, "\n")

# Add in a is_control column
conditions = [
    df["product"] == control_product,
    df["product"] != control_product
    ]
choices = [
    1, 0
    ]
df["is_control_product"] = np.select(conditions, choices)

