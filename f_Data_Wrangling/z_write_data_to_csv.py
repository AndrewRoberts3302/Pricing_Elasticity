#from pathlib import Path
from c_Data_Path.a_data_path import data_path
from f_limit_the_columns import df

#cwd = Path(__file__).parent
df.to_csv(data_path / "data_wrangled.csv", index=False)

print(df.head(5))