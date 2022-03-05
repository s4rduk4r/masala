import numpy as np

def bins_by_rice(sample_size : int) -> int:
    """Количество столбцов по правилу Райса

    Args:
        sample_size (int): размер выборки

    Returns:
        int: количество столбцов
    """
    return round(2 * np.power(sample_size, 1 / 3))