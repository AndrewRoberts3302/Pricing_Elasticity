import pandas as pd
from connection import engine

sql_query_epos_recent_dates = f"""
select distinct top 3 D_DateKey as date
from WS_LIVE.dbo.vw_Epos_Weekly
where D_DateId > 20230501
order by date desc;
"""

df_epos_recent_dates = pd.read_sql(sql_query_epos_recent_dates, engine)

print("\nThe most recent dates in Epos Weekly are:\n", df_epos_recent_dates, "\n")
