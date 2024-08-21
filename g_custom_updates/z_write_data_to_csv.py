#from pathlib import Path
from c_Data_Path.a_data_path import data_path

from y_clean_columns import df

# cwd = Path(__file__).parent
df.to_csv(data_path / "data_custom.csv", index=False)
