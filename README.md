[![License: MIT](https://img.shields.io/github/license/JRamonHA/Explorador-Meteorologico?style=flat-square)](https://github.com/JRamonHA/Explorador-Meteorologico/blob/main/LICENSE)
[![Top Language](https://img.shields.io/github/languages/top/JRamonHA/Explorador-Meteorologico?style=flat-square)](https://github.com/JRamonHA/Explorador-Meteorologico)
[![Repo Size](https://img.shields.io/github/repo-size/JRamonHA/Explorador-Meteorologico?style=flat-square)](https://github.com/JRamonHA/Explorador-Meteorologico)
[![Contributors](https://img.shields.io/github/contributors/JRamonHA/Explorador-Meteorologico?style=flat-square)](https://github.com/JRamonHA/Explorador-Meteorologico/graphs/contributors)

# Explorador Meteorológico

**Explorador Meteorológico** es una web app diseñada para el análisis y visualización de datos de RUOA y ESOLMET.  
El proyecto se desarrolla utilizando [Shiny for Python](https://shiny.posit.co/py/) y se apoya con SQL para la gestión de bases de datos.

## Tabla de contenido

- [.gitignore](.gitignore) - Archivos y carpetas a excluir de Git
- [requirements.txt](requirements.txt) - Dependencias del proyecto
- [config/](config/)
  - [config.py](config/config.py) - Variables globales, configuración de la app, etc.
- [data/](data/)
  - [raw/](data/001_raw/) - Datos sin procesar
  - [intermediate/](data/002_intermediate/) - Datos en nivel intermedio de procesamiento
  - [processed/](data/003_processed/) - Datos procesados listos para usar en la app
- [img/](img/) - Imágenes, gráficos y recursos visuales
- [scripts/](scripts/) - Scripts para análisis exploratorio, pruebas y desarrollo interactivo
- [app.py](app.py) - Archivo principal que inicia la aplicación Shiny para Python
- [components/](components/) - Componentes o módulos reutilizables de la app (widgets, layouts, etc.)
- [utils/](utils/) - Funciones y utilidades generales (p.ej., manejo de base de datos, validaciones, etc.)
- [tests/](tests/) - Pruebas unitarias e integradas
