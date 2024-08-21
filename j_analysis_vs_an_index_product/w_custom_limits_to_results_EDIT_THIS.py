import pandas as pd

from v_results_cleaning import results

# This file is to allow only the products through that are needed to be, or asked for in the brief.

#######################################################################################################################
# You can use this part of the script to find the products you want.
# p = results[["product"]]
# p = p[p["product"].str.contains("Operator")] # Edit this part
# p = p.drop_duplicates()
# print("\nThe products containing the search string are:\n", p, "\n")
#######################################################################################################################

#######################################################################################################################
# You can use this part of the script to list all of the products in the data.
# p = results[["product"]]
# p = p.drop_duplicates()
# print("\nThe complete product list is:\n", p, "\n")
#######################################################################################################################
#850_LAD_and_Wine_vs_Spirits

# results = results[
#     results["product"].isin(
#         [
#             "Productn Group | LAD | Pint",
#             "Product Group | Wine | 175ml",
#         ]
#     )
# ]





#######################################################################################################################
# 0601 HUK Pricing Elasticity - part 1
# results = results[
#     results["product"].isin(
#         [
#             "Product | Aspall Cyder | Pint",
#             "Product | Birra Moretti | Pint",
#             "Product | Cruzcampo | Pint",
#             "Product | Heineken Premium | Pint",
#             "Product | Inchs | Pint",
#             "Product | Madri Excepcional | Pint",
#             "Product | Orchard Thieves Apple Cider | Pint",
#             "Product | Stella Artois | Pint",
#             "Product | Strongbow | Pint",
#             "Product | Thatchers Gold | Pint"
#         ]
#     )
# ]
#######################################################################################################################

#######################################################################################################################
# SB144 CMBC Lager Pricing Elasticity
# results = results[
#     results["product"].isin(
#         [
#             "Product Class | Core Premium | Pint",
#             "Product Class | Core World | Pint",
#             "Product Class | Premium World | Pint",
#
#             "Product | Stella Artois | Pint",
#             "Product | Kronenbourg 1664 | Pint",
#             "Product | Heineken Premium | Pint",
#             "Product | San Miguel | Pint",
#             "Product | Birra Moretti | Pint",
#             "Product | Madri Excepcional | Pint",
#             "Product | Peroni Nastro Azzurro | Pint",
#             "Product | Estrella Damm | Pint",
#             "Product | Birrificio Angelo Poretti | Pint",
#             "Product | Camden Hells Lager | Pint",
#             "Product | Asahi Super Dry | 330ml",
#             "Product | Asahi Super Dry | Pint",
#             "Product | Asahi Super Dry 0.0 | 330ml"
#
#         ]
#     )
# ]
#######################################################################################################################

#######################################################################################################################
# SB169 MCBC Lager Pricing Elasticity
# results = results[
#     results["product"].isin(
#         [
#             "Product | Coors | Pint",
#             "Product Class | Core Standard | Pint"
#         ]
#     )
# ]
#######################################################################################################################