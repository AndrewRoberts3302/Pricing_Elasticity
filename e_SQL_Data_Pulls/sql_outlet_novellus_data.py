import pandas as pd

from connection import engine

# Collect Novellus regions and segment

sql_query = f"""
select distinct OT_CGAIdent as outlet,
    OT_SL2_Novellus as segment,
    OT_TL2_Novellus as region,
    OT_Quality_CGA as quality
from OI_LIVE.dbo.vw_Outlet
where OT_TL5_ISBA = N'GB'
  and OT_TL2_Novellus != N'Unknown'
  and OT_SL2_Novellus != N'Unclassified Segment'
"""

df_outlet = pd.read_sql(sql_query, engine)
