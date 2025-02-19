import pandas as pd

# Archivo de prueba que sé que tiene filas duplicadas
f = '../data/001_raw/windsensor.csv'
data = pd.read_csv(
    f, 
    # skiprows=[0, 2, 3], 
    index_col=0, 
    parse_dates=True, 
    # dayfirst=True
    )

def check_duplicate_rows(data):
    """
    Verifica si hay filas duplicadas en un DataFrame basado en sus índices.
    Args:
        data (pandas.DataFrame): El DataFrame a verificar.
    Returns:
        None: Si hay filas duplicadas, imprime los índices duplicados y las filas correspondientes.
    """
    if data.index.duplicated().any():
        # Obtiene todos los índices duplicados (incluye todas las ocurrencias)
        duplicated_indexes = data.index[data.index.duplicated(keep=False)]
        print("Índices duplicados:")
        print(duplicated_indexes.unique())
        
        # Muestra todas las filas cuyos índices están duplicados
        duplicated_rows = data.loc[duplicated_indexes]
        print("\nFilas duplicadas:")
        print(duplicated_rows.to_string())

check_duplicate_rows(data)