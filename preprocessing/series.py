import pandas as pd

def max_rows(*series : pd.Series) -> pd.Series:
    """Нахождение максимума между элементами рядов pandas.Series
    
    Оба ряда должны иметь одинаковые индексы

    Args:
        *series (pd.Series): Ряды сравнения

    Returns:
        pd.Series: Ряд, содержащий максимум для данной строки
    """
    d = dict()
    for s in range(len(series)):
        d[s] = series[s]
        
    return pd.DataFrame(
        data = d
    ).max(axis = 1)
