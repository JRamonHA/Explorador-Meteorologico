#%% 
import data_testing as dt

#%% Prueba de si es CSV]
f ="../data/001_raw/ESOLMET/2010_ESOLMET.csv" 
tag_endswith = dt.detect_endswith(f)

#%% Prueba si es UTF-8
data, tag_encoding = dt.import_data(f)

#%% Detecta si hay nans 
tag_nans = dt.detect_nans(data)

#%%
tag_duplicates = dt.detect_duplicates(data)

#%%
columnas = data.columns
columns_expected_type = {columna: 'float64' for columna in columnas}
tag_dtypes = dt.detect_dtype(columns_expected_type, data)

#%% Construye diccionario de pruebas
tests = {
    "CSV extension":tag_endswith,
    "Encoding UTF-8":tag_encoding,
    "Nans":tag_nans,
    "Duplicates":tag_duplicates,
    "Types":tag_dtypes
}

tests