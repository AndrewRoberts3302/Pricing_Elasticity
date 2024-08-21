import pandas as pd

from connection import engine

sql_query = f"""
select distinct OT_CGAIdent as outlet,
  OT_SegmentationLevel1Description as segment
from OI_LIVE.dbo.vw_Outlet_HUK
where OT_CGAIdent > 0
  and OT_SegmentationLevel1Description is not null
  and OT_TL5_ISBA = N'GB';
"""

df_outlet_segment_huk = pd.read_sql(sql_query, engine)