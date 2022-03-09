# masala.preprocessing.series
Helper functions to preprocess `pandas.Series` objects
---
- [masala.preprocessing.series.max_rows](#masala_hypotheses_categorical_pairwise_fisher)

## <a id="masala_hypotheses_categorical_pairwise_fisher">masala.preprocessing.series.max_rows(*series)</a>
Elementwise maximum between the rows of two and more `pandas.Series` objects. Rationale behind this function is to compare series from two and more different dataframes which have the same index values

All series must have the same `index` values

**Parameters:** 
__*series (pandas.Series):__ Series to compare


**Returns:** **pandas.Series** object with maximum values from the `*series` arguments in each row
