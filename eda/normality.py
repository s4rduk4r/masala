import pandas as pd
from scipy.stats import normaltest, shapiro
from masala.pretty_msg import print_msg, print_warn

# Обёртка над тестом на нормальность по д'Агостино-Пирсону
def normality_test(s : pd.Series, alpha : float = 0.05, method : str = None, verbose : bool = False) -> tuple:
    """Тест на нормальность
    
    По-умолчанию автоматически выбирает метод Шапиро-Уилка (n <= 5000) или д'Агостино-Пирсона (n > 5000), 
    в зависимости от размера выборки (n).

    Args:
        s (pd.Series): Случайная величина с типом pandas.Series
        alpha (float, optional): Уровень значимости. Defaults to 0.05.
        method (str, optional): Метод для проверки на нормальность. По-умолчанию None.
                None - выбрать метод автоматически
                d_agostino-pearson - принудительно использовать метод д'Агостино-Пирсона
                shapiro-wilk - принудительно использовать метод Шапиро-Уилка
        
        verbose (bool): Вывод результата сравнения p-значения с уровнем значимости alpha

    Returns:
        statistic, p_value - значение статистики метода и p-значение
    """
    # Автоматический выбор метода, в зависимости от размера выборки
    if method is None:
        if len(s) > 5000:
            method = "d_agostino-pearson"
        else:
            method = "shapiro-wilk"

    # Применение метода
    if method == "d_agostino-pearson":
        s_value, p_value = normaltest(s.to_numpy(), nan_policy = "omit")
    elif method == "shapiro-wilk":
        s_value, p_value = shapiro(s.to_numpy())
    
    # Вывод интерпретации на экран
    if verbose:
        if p_value > alpha:
            print_msg("Normal distribution")
        else:
            print_warn("Non-normal distribution")
    return (s_value, p_value)
