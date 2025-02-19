import pandas as pd

f = '../data/001_raw/RUOA/Datos_hora/2016_RUOA_HR.csv'
data = pd.read_csv(
    f, 
    skiprows=[0, 2, 3], 
    index_col=0, 
    parse_dates=True, 
    dayfirst=True
    )

# del data['RECORD']

columnas = data.columns
columns_expected_type = {columna:'float64' for columna in columnas}

def check_column_type(columns_expected_type, data):
    """
    Verifica que los tipos de datos de las columnas en un DataFrame coincidan con los tipos esperados.
    Args:
        columns_expected_type (dict): Un diccionario donde las claves son los nombres de las columnas,
        y los valores son los tipos de datos esperados como cadenas de texto.
        data (pandas.DataFrame): El DataFrame que contiene los datos a verificar.
    Returns:
        None: La función imprime un mensaje si hay discrepancias entre los tipos esperados y los obtenidos.
    """
    columns_obtained_type = {columna:f'{data[columna].dtype}' for columna in columnas}

    for key in set(columns_expected_type.keys()).union(columns_obtained_type.keys()):
        expected = columns_expected_type.get(key, None)
        obtained = columns_obtained_type.get(key, None)
        
        if expected != obtained:
            print(f"En la columna '{key}' se espera: {expected}\nPero se obtuvo: {obtained}")

check_column_type(columns_expected_type, data)