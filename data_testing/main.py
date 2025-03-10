from typing import Optional, Tuple, Dict
import pandas as pd
import glob

def import_data(f: str, encoding: str = "utf-8") -> Tuple[Optional[pd.DataFrame], bool]:
    """
    Imports data from a CSV file, skipping specific rows and parsing dates.
    Args:
        f (str): The file path to the CSV file.
        encoding (str, optional): The encoding of the CSV file. Defaults to "utf-8".
    Returns:
        Tuple[Optional[pd.DataFrame], bool]: A tuple containing the DataFrame with the imported data (or None if an error occurred) and a boolean indicating if the encoding was correct.
    """
    try:
        data = pd.read_csv(
            f,
            skiprows=[0, 2, 3],
            index_col=0,
            parse_dates=True,
            dayfirst=True,
            encoding=encoding
        )
        del data["RECORD"]
        tag_encoding = True
    except Exception:
        data = None
        tag_encoding = False
        print(f"Revisa que el encoding sea {encoding}")

    return data, tag_encoding


def detect_endswith(filepath):
    """
    Detects the type of file based on its extension.
    Parameters:
        filepath (str): The path to the file to be checked.
    Returns:
        bool: True if the file ends with '.csv', False otherwise.
    """
    if filepath.endswith('.csv'):
        tag_endswith = True
    else:
        tag_endswith = False
        print("El archivo no termina en csv")
        
    return tag_endswith


def detect_nans(df : pd.DataFrame) -> bool:
    """
    Detects if a DataFrame contains any NaN values.
    Parameters:
        df (pd.DataFrame): The DataFrame to check for NaN values.
    Returns:
        bool: True if there are no NaN values in the DataFrame, False otherwise.
    """
    if df.isnull().sum().sum() == 0:
        tag_nans = True
    else:
        tag_nans = False

    return tag_nans


def detect_duplicates(df: pd.DataFrame) -> bool:
    """
    Checks if a DataFrame contains duplicate rows based on its index.
    
    Parameters:
        df (pd.DataFrame): The DataFrame to check for duplicate rows.
    
    Returns:
        bool: True if there are no duplicate rows; False if duplicate rows exist.
    """
    if df.index.duplicated().any():
        tag_duplicates = False
    else:
        tag_duplicates = True

    return tag_duplicates


def detect_dtype(columns_expected_type: Dict[str, str], data: pd.DataFrame) -> bool:
    """
    Verifies that the data types of the DataFrame columns match the expected types.
    
    Parameters:
        columns_expected_type (Dict[str, str]): A dictionary where the keys are the column names and the values 
                                                  are the expected data types (as strings).
        data (pd.DataFrame): The DataFrame containing the data to verify.
    
    Returns:
        bool: True if all column types match the expected types; False if any mismatch is found.
    """
    for col in columns_expected_type:
        if col not in data.columns:
            raise KeyError(f"Column '{col}' does not exist in the DataFrame.")

    columns_types = {col: str(data[col].dtype) for col in data.columns}

    tag_dtypes = True

    for col in set(columns_expected_type.keys()).union(columns_types.keys()):
        expected = columns_expected_type.get(col)
        obtained = columns_types.get(col)
        if expected != obtained:
            tag_dtypes = False
            break

    return tag_dtypes


def compare(path, extension):
    """
    Reads all files with a specific extension in the given directory,
    and compares the columns of each file with those of the first file read, which is used as a reference.
    
    Args:
        path (str): Path to the directory containing the CSV files.
        extension (str): Extension of the files to read (e.g., 'csv').
    
    Returns:
        None: The function prints the results of the column comparison to the console.
    """
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
            extra = columns.difference(reference_columns)    # Columnas que tiene el archivo actual de más

            print(f"\nComparación para {file}:")
            print(f"Columnas comunes: {common}")
            print(f"Columnas faltantes (en referencia): {missing}")
            print(f"Columnas extra (en archivo): {extra}")

            if columns == reference_columns:
                print(f"{file} coincide con la referencia.")
            else:
                print(f"{file} no coincide con la referencia.")