[![License: MIT](https://img.shields.io/github/license/JRamonHA/Explorador-Meteorologico?style=flat-square)](https://github.com/JRamonHA/Explorador-Meteorologico/blob/main/LICENSE)

# Explorador Meteorológico

**Explorador Meteorológico** es una web app diseñada para el análisis y visualización de datos de RUOA y ESOLMET.  
El proyecto se desarrolla utilizando [Shiny for Python](https://shiny.posit.co/py/) y se apoya con SQL para la gestión de bases de datos.

## Tabla de contenido

- [README.md](README.md) - Descripción general y guía de inicio
- [.gitignore](.gitignore) - Archivos y carpetas a excluir de Git
- [requirements.txt](requirements.txt) - Dependencias del proyecto (Python)
- [config/](config/)
  - [config/config.py](config/config.py) - Variables globales, configuración de la app, etc.
- [data/](data/)
  - [data/raw/](data/raw/) - Datos sin procesar
  - [data/processed/](data/processed/) - Datos procesados listos para usar en la app
- [img/](img/) - Imágenes, gráficos y recursos visuales
- [scripts/](scripts/) - Scripts para análisis exploratorio, pruebas y desarrollo interactivo
- [src/](src/)
  - [src/app.py](src/app.py) - Archivo principal que inicia la aplicación Shiny para Python
  - [src/components/](src/components/) - Componentes o módulos reutilizables de la app (widgets, layouts, etc.)
  - [src/utils/](src/utils/) - Funciones y utilidades generales (p.ej., manejo de base de datos, validaciones, etc.)
- [tests/](tests/) - Pruebas unitarias e integradas
