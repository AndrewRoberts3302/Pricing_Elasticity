"""
This script givs you beer qualities:

ECONOMY, MAINSTREAM, PREMIUM, SUPPERPREMIUM
"""

import pandas as pd

from connection import engine

# Collect product id and product data

sql_query = f"""
select distinct ProductItemId as pm_product_item_id,
  ProductDescription as product,
  PT_MBUKCat as product_class,
  ClassificationLevel4Description as product_group
from GB_BI_DATA_LIVE.dbo.vw_MILLER_LAD_A
where D_CGAPeriod >= 233 -- Jan 2024
  and ClassificationLevel4Description = N'Beer'
"""

df_product_miller = pd.read_sql(sql_query, engine)
