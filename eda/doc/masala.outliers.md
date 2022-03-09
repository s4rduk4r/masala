# masala.eda.outliers
Outliers detection methods
---
- [masala.eda.outliers.outliers_rm_by_sample_iqr](#masala_eda_outliers_outliers_rm_by_sample_iqr)
- [masala.eda.outliers.outliers_rm_by_carling](#masala_eda_outliers_outliers_rm_by_carling)

## <a id="masala_eda_outliers_outliers_rm_by_sample_iqr">eda.outliers.outliers_rm_by_sample_iqr(s)</a>
Interquartile range outlier detection method.

Observable is marked as outlier if it doesn't belong to the range of [q1 - 1.5 $\cdot$ (q3 - q1); q3 + 1.5 $\cdot$ (q3 - q1)], where q1 - 1st quartile; q3 - 3rd quartile 

**Parameters:**

**s (pandas.Series):** Sample of continuous random variable

**Returns:** **pandas.Series**

    Returns boolean series with False values marking outliers and True values marking statistically significant observables

---
## <a id="masala_eda_outliers_outliers_rm_by_carling">eda.outliers.outliers_rm_by_carling(s)</a>
Interquartile range outlier detection method with [Carling's correction](https://www.researchgate.net/profile/Kenneth-Carling/publication/4894204_Resistant_outlier_rules_and_the_non-Gaussian_case/links/59eafa2b0f7e9bfdeb6ce138/Resistant-outlier-rules-and-the-non-Gaussian-case.pdf)

Observable is marked as outlier if it doesn't belong to the range of [M - k $\cdot$ (q3 - q1); M + k $\cdot$ (q3 - q1)],<br>where
- M - sample median
- q1 - upper true quarth
- q3 - lower true quarth
- k - factor dependent on a sample size

**Parameters:**

**s (pandas.Series):** Sample of continuous random variable

**Returns:** **pandas.Series**

> Returns boolean series with False values marking outliers and True values marking statistically significant observables
