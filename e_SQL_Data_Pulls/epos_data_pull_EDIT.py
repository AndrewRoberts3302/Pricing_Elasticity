"""
You can edit the predicates in this when needed, for example:
You may want to limit to product to spirits or LADs.
"""

import pandas as pd

from connection import engine

# Collect the data

sql_query = f"""
with c as
(
select distinct D_DateKey as date,
    OT_CGAIdent as outlet,
    OT_Operator as operator,
	PM_ProductItemId as pm_product_item_id,
	PM_UOMDescription as pm_uom_description,
	sum(F_SalesQuantity) as quantity,
	sum([F_SalesValue_£]) as value,
	sum([F_SalesVolume_MLS]) as volume
from WS_LIVE.dbo.vw_Epos_Weekly
where D_DateId >= 20230701
    and D_DateId < 20240801
    and F_SalesQuantity > 0
    and [F_SalesValue_£] > 0
    and PT_ClassificationLevel6Description in (N'LAD', N'Spirits', N'Wine/Champagne') -- Edit this when needed
group by D_DateKey,
    OT_CGAIdent,
    OT_Operator,
	PM_ProductItemId,
	PM_UOMDescription
)
select distinct outlet,
    operator,
	pm_product_item_id,
	pm_uom_description,
	avg(quantity) as quantity,
	avg(value) as value, 
	avg(volume) as volume
from c
group by outlet,
    operator,
	pm_product_item_id,
	pm_uom_description;
"""

df_data = pd.read_sql(sql_query, engine)
