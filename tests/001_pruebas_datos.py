#%% 
import data_testing as dt

#%% Prueba de si es CSV]
f ="../data/001_raw/ESOLMET/2015_ESOLMET.csv" 
tag_endswith = dt.detect_endswith(f)

#%% Prueba si es UTF-8
data, tag_encoding = dt.import_data(f)

#%% Detecta si hay nans 
tag_nans = dt.detect_nans(data="JoseRra")

#%% Construye diccionario de pruebas
tests = {
    "CSV extension":tag_endswith,
    "Encoding UTF-8":tag_encoding,
    "Nans":tag_nans,
    # "Nans":
}

tests
