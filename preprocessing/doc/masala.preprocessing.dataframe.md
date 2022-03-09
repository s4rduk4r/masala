# masala.preprocessing.dataframe
Helper functions to preprocess `pandas.DataFrame` objects
---
- [masala.preprocessing.dataframe.open_dataset](#masala_preprocessing_dataframe_open_dataset)
- [masala.preprocessing.dataframe.na_counts_and_props](#masala_preprocessing_dataframe_na_counts_and_props)

## <a id="masala_preprocessing_dataframe_open_dataset">preprocessing.dataframe.open_dataset(uri_local, uri_remote, tsv)</a>
Open CSV or TSV file locally or remotely. This function is a thin wrapper over `pandas.read_csv()`

**Parameters:**

**tsv (bool)**: True - open file as TSV, False - open file as CSV


**Returns:** 

**pandas.DataFrame** if file open is a success<br>
**None** - if file open has failed

---
## <a id="masala_preprocessing_dataframe_na_counts_and_props">preprocessing.dataframe.na_counts_and_props(df, sort_by_props = True, background_gradient = True)</a>

Count misses and calculate their proportion in a dataset

**Parameters:**

**df (pd.DataFrame):** dataset

**sort_by_props (bool):** sort output by proportions

**background_gradient (bool):** fill cells background color as value gradient


**Returns:** **pandas.DataFrame** object with columns `na_counts`, `na_props` with NA counts and NA proportions in `df`
