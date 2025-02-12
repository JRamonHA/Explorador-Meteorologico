import pandas as pd
import glob

def compare_file_columns(path, extension):
    # Obtiene todos los archivos con la extensión indicada en el directorio especificado
    files = glob.glob(f'{path}/*.{extension}')
    
    # Diccionario para almacenar columnas de cada archivo
    file_columns = {}

    for file in files:
        # Si el nombre del archivo contiene "2022" o "2023", se lee sin skiprows
        if "2022" in file or "2023" in file:
            df = pd.read_csv(file, encoding='ANSI', index_col=0, parse_dates=True, low_memory=False)
        else:
            df = pd.read_csv(file, encoding='ANSI', skiprows=[0, 2, 3],
                             index_col=0, parse_dates=True, dayfirst=True, low_memory=False)
        
        # Almacena las columnas del DataFrame
        file_columns[file] = set(df.columns)
    
    # Compara columnas entre archivos usando el primero como referencia
    reference_columns = None
    for file, columns in file_columns.items():
        if reference_columns is None:
            reference_columns = columns
            print(f"\n{file} se usa como referencia con columnas: \n{columns}")
        else:
            # Calcula las columnas comunes y las diferencias
            common = reference_columns.intersection(columns)
            missing = reference_columns.difference(columns)  # Columnas que faltan en el archivo actual
            extra = columns.difference(reference_columns)      # Columnas que tiene el archivo actual de más

            print(f"\nComparación para {file}:")
            print(f"Columnas comunes: {common}")
            print(f"Columnas faltantes (en referencia): {missing}")
            print(f"Columnas extra (en archivo): {extra}")

            if columns == reference_columns:
                print(f"{file} coincide con la referencia.")
            else:
                print(f"{file} no coincide con la referencia.")

compare_file_columns('../data/001_raw/ESOLMET', 'csv')