# masala.eda.normality
Outliers detection algorithms
---
- [eda.normality.normality_test](#masala_eda_normality_assert_step)

## <a id="masala_eda_normality_assert_step">eda.normality.normality_test(s, alpha = 0.05, method = None, verbose = False)</a>
Normality test wrapper. By default automatically chooses between Shapiro-Wilk (n <= 5000) and d'Agostino-Pearson (n > 5000) normality test based on the sample size `n`

**Parameters:** 

**s (pandas.Series):** Sample of continuous random variable
    
**alpha (float, optional):** Significance level. Defaults to 0.05.

**method (str, optional):** Normality test method. Defaults to None.<br>Options:
- None - choose automatically
- d_agostino-pearson - force d'Agostino-Pearson method
- shapiro-wilk - force Shapiro-Wilk method

**verbose (bool):** Print p-value interpretation according to selected `alpha`

**Returns:** 
        statistic, p_value - method statistic value, p-value of the test

