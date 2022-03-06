import pandas as pd
import numpy as np

def outliers_rm_by_sample_iqr(s: pd.Series) -> pd.Series:
    """Метод исключения выбросов по межквартильному расстоянию выборки.
    
    Наблюдаемое является выбросом, если находится вне интервала [q1 - 1.5 * (q3 - q1); q3 + 1.5 *(q3 - q1)]
    
    q1 - 1-й квартиль выборки
    
    q3 - 2-й квартиль выборки 

    Args:
        s (pd.Series): выборка количественной переменной

    Returns:
        pd.Series:
        
        True = статистически значимое значение.
        False = выброс
    """
    q1 = s.quantile(0.25)
    q3 = s.quantile(0.75)
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    return s.apply(lambda x: True if lower <= x <= upper else False)

# Метод исключения выбросов по Карлингу
def outliers_rm_by_carling(s : pd.Series) -> pd.Series:
    """Метод исключения выбросов по [Карлингу [1]](https://www.researchgate.net/profile/Kenneth-Carling/publication/4894204_Resistant_outlier_rules_and_the_non-Gaussian_case/links/59eafa2b0f7e9bfdeb6ce138/Resistant-outlier-rules-and-the-non-Gaussian-case.pdf).
    
    Наблюдаемое является выбросом, если находится вне интервала [M - k * (q3 - q1); M + k * (q3 - q1)]
    
    M - медиана выборки
    
    q1 - верхняя истинная четверть
    
    q3 - нижняя истинная четверть
    
    k - коэффициент, зависящий от размера выборки

    Args:
        s (pd.Series): выборка количественной переменной

    Returns:
        pd.Series: 
        True = статистически значимое значение.
        False = выброс
        
    References:
    
        1. Carling K. Resistant outlier rules and the non-Gaussian case. Computational Statistics & Data Analysis. (2000). 33(3). pp.249-258.
    """
    # Ранжируем данные
    s = s.sort_values().reset_index(name = "value")
    s_ranked = s.value
    # Среднее
    mu = s_ranked.median()
    # Параметры
    n = s_ranked.shape[0]
    h = n / 4 + 5 / 12
    j = round(np.floor(h)) - 1
    i = n - j - 1
    h = h - j - 1
    k = (17.63 * n - 23.64) / (7.74 * n - 3.71)
    # Оценки квартилей и межквартильного расстояния
    q1 = (1 - h) * s_ranked[j] + h * s_ranked[j + 1]
    q3 = (1 - h) * s_ranked[i] + h * s_ranked[i - 1]
    iqr = q3 - q1
    # Границы статистически значимых величин
    lower, upper = mu - k * iqr, mu + k * iqr
    # False = выброс
    s_ranked = s_ranked.apply(lambda x: True if lower <= x <= upper else False)
    # Восстановить исходные индексы
    s_ranked.index = s.loc[:, "index"]
    return s_ranked 