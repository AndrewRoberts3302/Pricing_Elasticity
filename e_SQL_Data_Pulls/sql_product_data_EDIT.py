"""
You can edit this when needed, for example:
You may want to use product level 6 for spirits projects but product level 5
for beer projects.
"""

import pandas as pd

from connection import engine

# Collect product id and product data

sql_query = f"""
select distinct PM_ProductItemId as pm_product_item_id,
PT_ProductDescription as product,
PT_ClassificationLevel5Description as product_class,
case 
  when PT_ClassificationLevel5Description = N'Cocktails' then PT_ClassificationLevel5Description
  when PT_ClassificationLevel6Description = N'Spirits' and PT_ClassificationLevel5Description != N'Cocktails' then N'Spirits exc Cocktails'
  else PT_ClassificationLevel6Description 
end as product_group  -- Edit when required.
from PL_LIVE.dbo.vw_ProductImport order by pm_product_item_id asc;
"""

df_product = pd.read_sql(sql_query, engine)
