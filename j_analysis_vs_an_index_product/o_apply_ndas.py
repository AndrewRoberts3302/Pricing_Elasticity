from pathlib import Path
from n_merge_results import results

print("\n-------------------------------------------------------------------\n")
print("RUNNING FILE:", Path(__file__).name)
print("\n-------------------------------------------------------------------\n")

results = results.loc[
    (
        (results["outlet_count"] >= 50) &
        (results["operator_count"] >= 3) &
        (results["nda_share"] <= 0.5)
    )
]
