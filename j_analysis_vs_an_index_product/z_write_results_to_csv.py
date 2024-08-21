from c_Data_Path.a_data_path import data_path

from y_append_results_copy_with_high_outlet_counts import results, list_price_difference_bands

results.to_csv(data_path / "results_vs_control.csv", index=False)
list_price_difference_bands.to_csv(data_path / "list_price_difference_bands.csv", index=False)
u = results['product'].unique()
print('The unique products in df are: \n', sorted(u), '\n')
