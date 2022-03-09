# masala.eda.histogram
Helper functions to build histograms
---
- [histogram.bins_by_rice](#masala_eda_histogram_bins_by_rice)
- [histogram.plot_hist](#masala_eda_histogram_plot_hist)

## <a id="masala_eda_histogram_bins_by_rice">eda.histogram.bins_by_rice(sample_size)</a>
Bins count according to the Rice rule

**Parameters:** **sample_size: int**

    Sample size

**Returns:** int: bins count

---
## <a id="masala_eda_histogram_plot_hist">eda.histogram.plot_hist(s, title = None, xlabel = None, ylabel = None, scale_factor_x = 1.0, scale_factor_y = 1.0, rm_outliers = False, x_range = None)</a>
Bins count according to the Rice rule

**Parameters:** **s (pd.Series)** Sample
**title (str, optional):**
    Histogram title. Defaults to None.
    
**xlabel (str, optional):**

    x-axis title. Defaults to None.

**ylabel (str, optional):**
    
    y-axis title. Defaults to None.

**scale_factor_x (float, optional):**
    
    x-axis ticks scale factor. Defaults to 1.0.

**scale_factor_y (float, optional):**

    y-axis ticks scale factor. Defaults to 1.0.

**rm_outliers (bool, optional):**

    remove outliers. Defaults to False.

**x_range (tuple, optional):**

    set range of x-axis ticks. Same as `range=` in matplotlib.pyplot. Defaults to None.

**Returns:** **int:** bins count

