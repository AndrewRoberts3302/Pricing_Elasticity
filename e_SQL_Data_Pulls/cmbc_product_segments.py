import pandas as pd

from connection import engine

# Collect CMBC product segments

sql_query = f"""
select distinct ProductItemId as product_item_id,
    ProductId as product_id,
	ProductDescription as product,
	PT_Segment as cmbc_product_segment,
	PT_SubSegment as cmbc_product_sub_segment,
	PT_Format as serve_format,
	UoMDescription as uom
from GB_BI_DATA_LIVE.dbo.vw_CUK_PCW_B
where D_DateKey > '2023-01-01';
"""

cmbc_product_segments = pd.read_sql(sql_query, engine)