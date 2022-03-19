import pandas as pd
import matplotlib.pyplot as plt

from masala.pretty_msg import print_msg
from masala.eda.histogram import bins_by_rice
from masala.eda.normality import normality_test
from masala.eda.outliers import outliers_rm_by_carling

"""
Алгоритм EDA

1. Гистограмма исходных данных
2. Количество выбросов и диапазон их значений
3. Гистограмма без выбросов
4. Проверка на нормальность очищенных данных
5. Описательная статистика
"""
def make_eda(s : pd.Series, title : str, xlabel : str, ylabel : str, scale_x : float, scale_y : float) -> None:
    """
    Algorithm of EDA

    1. Plot histogram of raw data
    2. Detect outliers, count them and present their bounds
    3. Plot histogram of a clean data
    4. Normality check for a clean data
    5. Descriptive statistics of a clean data

    Args:
        s (pd.Series): sample
        title (str): histogram title
        xlabel (str): X-axis histogram title
        ylabel (str): Y-axis histogram title
        scale_x (float): X-axis ticks factor
        scale_y (float): Y-axis ticks factor
    """
    s_clean = s[outliers_rm_by_carling(s)]
    
    # Plot graphs
    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))
    
    ax[0].hist(x = s, bins = bins_by_rice(s.shape[0]))
    ax[0].set_title("Raw data")
    ax[0].set_xlabel(xlabel)
    ax[0].set_ylabel(ylabel)
    
    ax[1].boxplot(s)
    
    ax[2].hist(x = s_clean, bins = bins_by_rice(s_clean.shape[0]))
    ax[2].set_title("Clean data histogram")
    ax[2].set_xlabel(xlabel)
    ax[2].set_ylabel(ylabel)
    
    # Adjust scales
    if scale_x > 1:
        ax[0].set_xticklabels(["{:.1f}".format(x / scale_x) for x in plt.gca().get_xticks()])
        ax[2].set_xticklabels(["{:.1f}".format(x / scale_x) for x in plt.gca().get_xticks()])
    if scale_y > 1:
        ax[0].set_yticklabels(["{:.1f}".format(y / scale_y) for y in plt.gca().get_yticks()])
        ax[2].set_yticklabels(["{:.1f}".format(y / scale_y) for y in plt.gca().get_yticks()])
    
    fig.suptitle(title)
    fig.tight_layout()
    
    plt.show()
    
    print()
    print_msg("Outliers statistics")
    
    display(s[~outliers_rm_by_carling(s)].agg([min, max, "count"]))
    
    print_msg("Normality check of clean data")
    
    normality_test(s_clean, verbose=True)
    
    print()
    print_msg("Descriptive statistics of clean data")
    s_desc = s_clean.describe()
    s_mode = s_clean.value_counts().head(1)
    display(
        pd.concat(
            [
                pd.DataFrame(data = {"value": s_desc}),
                pd.DataFrame(data = {"value" : s_mode.index, "freq" : s_mode.values}, index = ["mode"])
            ]
        )
    )