"""
Note that this is incorrect, Dev have never updated this in the databases.
There is an option to manually do this in the custom update directory.
"""

import pandas as pd

from connection import engine

# Collect Novellus regions and segment

sql_query = f"""
select distinct OT_CGAIdent as outlet,
  OT_SegmentationLevel1Description as segment
from OI_LIVE.dbo.vw_Outlet_Diageo
where OT_TL5_ISBA = N'GB';
"""

df_outlet_segment_diageo = pd.read_sql(sql_query, engine)
