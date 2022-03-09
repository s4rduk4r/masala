# masala.hypotheses.categorical
Helper functions to perform hypothesis test on categorical variables
---
- [hypotheses.categorical.pairwise_fisher](#masala_hypotheses_categorical_pairwise_fisher)
- [hypotheses.categorical.multiple_comparisons_chi2](#masala_hypotheses_categorical_multiple_comparisons_chi2)
- [hypotheses.categorical.prop_conf_int](#masala_hypotheses_categorical_prop_conf_int)

## <a id="masala_hypotheses_categorical_pairwise_fisher">hypotheses.categorical.pairwise_fisher(contingency_table, alpha = 0.05)</a>
Multiple pairwise comparisons (post-hoc) with Fisher's exact test from `scipy.stats`

Prints `pandas.DataFrame` with matrix of p-values between the comparison groups. Cells holding p-values $\le$ alpha are highlighted

Function is `pandas.DataFrame.pipe()` friendly

**Parameters:**

**contingency_table (pandas.DataFrame)**
Contingency table of shape (n, 2) where n - amount of comparison groups

**alpha (float, optional):** Significance level. Defaults to 0.05.


**Returns:** **pandas.DataFrame** Same as input argument `contingency_table`

---
## <a id="masala_hypotheses_categorical_multiple_comparisons_chi2">hypotheses.categorical.multiple_comparisons_chi2(contingency_table, alpha = 0.05)</a>
Multiple comparisons with Chi-square test from `scipy.stats`

Prints the result of Chi-square test for the comparison groups. If H1 is accepted, calls for post-hoc Fisher's exact test [pairwise_fisher()](#masala_hypotheses_categorical_pairwise_fisher)

Function is `pandas.DataFrame.pipe()` friendly

**Parameters:**

**contingency_table (pandas.DataFrame)**
Contingency table of shape (n, 2) where n - amount of comparison groups

**alpha (float, optional):** Significance level. Defaults to 0.05.


**Returns:** **pandas.DataFrame** Same as input argument `contingency_table`

---
## <a id="masala_hypotheses_categorical_prop_conf_int">prop_conf_int(df, column_success, column_failures)</a>
Proportions and their corresponding 95%-confidence intervals.

Formula implemented has been taken from here - https://www.biostathandbook.com/confidence.html

Function is `pandas.DataFrame.pipe()` friendly

**Parameters:**

**df (pandas.DataFrame)**
Contingency table of shape (n, 2) where n - amount of groups

**column_success (pandas.Index)**
Column name with successes

**column_failures (pandas.Index)**
Column name with failures

**Returns:** **pandas.DataFrame** with columns holding proportion, left confidence interval bound, right confidence interval bound

