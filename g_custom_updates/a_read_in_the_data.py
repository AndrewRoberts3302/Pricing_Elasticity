import pandas as pd
from c_Data_Path.a_data_path import data_path

# Set the console to display full contents of a DataFrame
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.width', None)

# Read in the pricing data.
data_wrangled = "data_wrangled.csv"
df = pd.read_csv(f"{data_path}/{data_wrangled}", parse_dates=["date"], low_memory=False)

# Read in Novellus region and segment data.
outlet_novellus_data = "outlet_novellus_data.csv"
ou_novellus = pd.read_csv(f"{data_path}/{outlet_novellus_data}")

# Read in CUK CMBC segmentation.
ou_cmbc = pd.read_csv("../b_Supplied_Data_Required/cuk_cmbc_outlet_segmentation.csv")

##############################################################################

# Read in the product data.
product_data = "product_data.csv"
df_product = pd.read_csv(f"{data_path}/{product_data}")


# Read in the custom product data.
# product_data = "0445_product_data_quality_blended_whisky.csv"
# product_data = "0445_product_data_flavoured_gin.csv"
# df_product = pd.read_csv(f"{data_path}/{product_data}")

##############################################################################
# Read in the custom products.
cmbc_product_data = "cmbc_product_data.csv"
custom_products = pd.read_csv(f"{data_path}/{cmbc_product_data}")

# Read in the Diageo custom segmentation data.
outlet_diageo_segment_data = "outlet_diageo_segment_data.csv"
ou_diageo = pd.read_csv(f"{data_path}/{outlet_diageo_segment_data}")

# Read in the HUK segment data.
outlet_data_huk_segment = "data_outlet_segment_huk.csv"
ou_huk = pd.read_csv(f"{data_path}/{outlet_data_huk_segment}")

# Read in the Miller beer qualities
# data_product_miller_beer_quality = "data_product_miller_beer_quality.csv"
# data_product_miller_beer_quality = pd.read_csv(f"{data_path}/{data_product_miller_beer_quality}")
