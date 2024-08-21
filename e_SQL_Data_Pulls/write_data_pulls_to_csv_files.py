# from pathlib import Path
from c_Data_Path.a_data_path import data_path

from sql_outlet_novellus_data import df_outlet
from cmbc_product_segments import cmbc_product_segments
from sql_product_data_EDIT import df_product
from epos_data_pull_EDIT import df_data
from sql_diageo_outlet_segments_NOT_USED import df_outlet_segment_diageo
from sql_huk_outlet_segments import df_outlet_segment_huk

# cwd = Path(__file__).parent

df_outlet.to_csv(data_path / "outlet_novellus_data.csv", index=False)
cmbc_product_segments.to_csv(data_path / "cmbc_product_data.csv", index=False)
df_outlet_segment_huk.to_csv(data_path / "data_outlet_segment_huk.csv", index=False)
df_product.to_csv(data_path / "product_data.csv", index=False)
df_data.to_csv(data_path / "data.csv", index=False)
# df_outlet_segment_diageo.to_csv(
#     data_path / "outlet_diageo_segment_data.csv", index=False)
