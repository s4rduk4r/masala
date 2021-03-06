import pandas as pd
from scipy.stats import normaltest, shapiro
from masala.pretty_msg import print_msg, print_warn

# Обёртка над тестом на нормальность по д'Агостино-Пирсону
def normality_test(s : pd.Series, alpha : float = 0.05, method : str = None, verbose : bool = False) -> tuple:
    """Normality test
    
    Chooses between Shapiro-Wilk by default (n <= 5000) or d'Agostino-Pearson (n > 5000) based on a sample size

    Args:
        s (pd.Series): Sample
        alpha (float, optional): Significance level. Defaults to 0.05.
        method (str, optional): Normality test method. Defaults to None.
                None - choose method based on a sample size
                d_agostino-pearson - force use of d'Agostino-Pearson method
                shapiro-wilk - force use of Shapiro-Wilk method
        
        verbose (bool): Print interpretation of a test result based on comparison of p-value and alpha

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
