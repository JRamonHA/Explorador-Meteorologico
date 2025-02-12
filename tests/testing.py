#%%
import pandas as pd
import glob

def compare_file_columns(path, extension):
    files = glob.glob(f'{path}/*.{extension}')

    # Diccionario para almacenar columnas de cada archivo
    file_columns = {}

    for file in files:
        df = pd.read_csv(file, encoding='ANSI', skiprows=[0, 2, 3], index_col=0, parse_dates=True, dayfirst=True, low_memory=False)
        file_columns[file] = set(df.columns)

    # Comparar columnas
    reference_columns = None
    for file, columns in file_columns.items():
        if reference_columns is None:
            reference_columns = columns
            print(f"{file} se usa como referencia con columnas: {columns}")
        else:
            if columns == reference_columns:
                print(f"{file} tiene las mismas columnas que la referencia.")
            else:
                print(f"{file} No tiene las mismas columnas que la referencia. Columnas: {columns}")

compare_file_columns('../data/001_raw/ESOLMET', 'csv')