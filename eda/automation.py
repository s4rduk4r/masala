import pandas as pd
import matplotlib.pyplot as plt

from masala.pretty_msg import print_msg
from masala.eda.histogram import plot_hist
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
    print_msg("Raw data")
    plot_hist(s, title, xlabel, ylabel, scale_x, scale_y)
        
    print()
    print_msg("Outliers statistics")
    s.plot.box()
    plt.show()
    
    display(s[~outliers_rm_by_carling(s)].agg([min, max, "count"]))
    
    print()
    print_msg("Clean data histogram")
    plot_hist(s, title, xlabel, ylabel, scale_x, scale_y, rm_outliers=True)
    
    print()
    print_msg("Normality check of clean data")
    s_clean = s[outliers_rm_by_carling(s)]
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