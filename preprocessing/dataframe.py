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
def na_counts_and_props(df : pd.DataFrame) -> pd.DataFrame:
    """Посчитать и показать количество пропусков и их долю в наборе данных

    Args:
        df (pd.DataFrame): исходный набор данных

    Returns:
        pd.DataFrame: датафрейм с колонками na_counts, содержащим количество пропусков;
        na_props - доля пропусков в общей выборке
    """
    return pd.DataFrame(
        data = {"na_counts" : df.isna().sum()[df.isna().sum() > 0], 
                "na_props" : df.isna().mean()[df.isna().sum() > 0]}
    ).style.format({"na_props": "{:.3%}"})
    
