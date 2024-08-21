from pathlib import Path
from m_merge_results import results
from c_Data_Path.a_data_path import data_path

print("\n-------------------------------------------------------------------\n")
print("RUNNING FILE:", Path(__file__).name)
print("\n-------------------------------------------------------------------\n")

# Export the results with NDAs.

results.to_csv(data_path / "nda_results.csv", index=False)

results = results.loc[
    (
        (results["outlet_count"] >= 50) &
        (results["operator_count"] >= 3) &
        (results["nda_share"] <= 0.5)
    )
]
