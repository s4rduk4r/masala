import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from masala.eda.outliers import outliers_rm_by_carling

def bins_by_rice(sample_size : int) -> int:
    """Количество столбцов по правилу Райса

    Args:
        sample_size (int): размер выборки

    Returns:
        int: количество столбцов
    """
    return round(2 * np.power(sample_size, 1 / 3))

# Обёртка над pandas.Series.hist
def plot_hist(
    s : pd.Series,
    title : str = None,
    xlabel : str = None,
    ylabel : str = None,
    scale_factor_x : float = 1.0,
    scale_factor_y : float = 1.0,
    rm_outliers = False,
    x_range = None):
    """Тонкая обёртка над pandas.Series.hist() для построения гистограмм

    Args:
        s (pd.Series): Выборка случайной величины
        title (str, optional): Название гистограммы. Defaults to None.
        xlabel (str, optional): Подпись по оси абсцисс. Defaults to None.
        ylabel (str, optional): Подпись по оси ординат. Defaults to None.
        scale_factor_x (float, optional): Масштабирование числовых отметок по оси абсцисс. Defaults to 1.0.
        scale_factor_y (float, optional): Масштабирование числовых отметок по оси ординат. Defaults to 1.0.
        rm_outliers (bool, optional): Убрать выбросы из выборки. Defaults to False.
        x_range (_type_, optional): Ограничить диапазон значений абсцисс. Задаётся идентично параметру range= в matplotlib.pyplot. Defaults to None.
    """
    #
    if rm_outliers:
        s = s[outliers_rm_by_carling(s)]
    s.hist(bins = bins_by_rice(s.shape[0]), range = x_range)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.gca().set_xticklabels(["{:.1f}".format(x / scale_factor_x) for x in plt.gca().get_xticks()])
    plt.gca().set_yticklabels([y / scale_factor_y for y in plt.gca().get_yticks()])
    plt.show()
    