# Masala

Little snippets for Jupyter Lab/Jupyter Notebook environments.

Intend is to automate some of the routine actions with pandas, numpy, scipy, matplotlib

## Usage
### Example 1
```python
from masala.asserts import assert_step

s = pd.Series([pd.NA, 2, 3, 4, 5])

assert_step(s.isna().sum() == 0)
```

### Example 2
```python
import masala.eda.histogram

s = pd.Series([1, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 8])
masala.eda.histogram.plot_hist(s, "My series", "X-axis", "Y-axis", 1, 1, False, None)
plt.show()
```

# API
---
## Utility
- [masala.asserts](doc/masala.asserts.md)
- [masala.pretty_msg](doc/masala.pretty_msg.md)

## Preprocessing
- [masala.preprocessing.dataframe](preprocessing/doc/masala.preprocessing.dataframe.md)
- [masala.preprocessing.series](preprocessing/doc/masala.preprocessing.series.md)

## EDA
- [masala.eda.histogram](eda/doc/masala.histogram.md)
- [masala.eda.normality](eda/doc/masala.normality.md)
- [masala.eda.outliers](eda/doc/masala.outliers.md)

## Hypothesis tests
- [masala.hypotheses.categorical](hypotheses/doc/masala.hypotheses.categorical.md)
