import pandas as pd

def max_rows(s1 : pd.Series, s2 : pd.Series) -> pd.Series:
    """Нахождение максимума между элементами рядов pandas.Series
    
    Оба ряда должны иметь одинаковые индексы

    Args:
        s1 (pd.Series): Первый ряд сравнения
        s2 (pd.Series): Второй ряд сравнения

    Returns:
        pd.Series: Ряд, содержащий максимум для данной строки
    """
    return pd.DataFrame(
        data = {"s1" : s1, "s2" : s2}
    ).max(axis = 1)
