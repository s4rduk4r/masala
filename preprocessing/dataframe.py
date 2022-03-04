import pandas as pd

# Открыть CSV или TSV файл, который может находиться локально или на сервере
def open_dataset(uri_local : str, uri_remote : str, tsv : bool = False) -> pd.DataFrame:
    """Попытка открыть файл локально или в контейнере

    Args:
        tsv (bool): Флаг, указывающий использовать пробелы в качестве разделителя

    Returns:
        pd.DataFrame: датафрейм в случае успешного открытия файла. None - в результате ошибки
    """
    df = None
    sep = "\t" if tsv else ","
    try:
        df = pd.read_csv(uri_local, sep=sep)
    except:
        df = pd.read_csv(uri_remote, sep=sep)
    return df

# Пропуски
def na_counts_and_props(df : pd.DataFrame, sort_by_props : bool = True, background_gradient : bool = True) -> pd.DataFrame:
    """Посчитать и показать количество пропусков и их долю в наборе данных

    Args:
        df (pd.DataFrame): исходный набор данных
        sort_by_props (bool) : сортировать вывод по возрастанию
        background_gradient (bool) : залить выходные значения градиентом

    Returns:
        pd.DataFrame: датафрейм с колонками na_counts, содержащим количество пропусков;
        na_props - доля пропусков в общей выборке
    """
    result = pd.DataFrame(
        data = {"na_counts" : df.isna().sum()[df.isna().sum() > 0], 
                "na_props" : df.isna().mean()[df.isna().sum() > 0]}
    )
    
    if sort_by_props:
        result = result.sort_values(by = "na_props")
    
    result.style.format({"na_props": "{:.3%}"})
    
    if background_gradient:
        result = result.style.background_gradient()
    return result
    
