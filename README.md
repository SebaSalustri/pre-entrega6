# Análisis climático con DuckDB

## Descripción

Proyecto de análisis de datos climáticos mediante Python, SQL y DuckDB.

El objetivo es demostrar cómo consultar directamente archivos CSV sin utilizar un servidor de base de datos tradicional.

## Tecnologías utilizadas

- Python
- DuckDB
- Pandas
- SQL

## Dataset

Se utiliza un conjunto de datos de ejemplo con registros de temperaturas de Valencia, Madrid y Barcelona durante 2024.

Los datos son ilustrativos y no representan mediciones meteorológicas oficiales.

## Instalación

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

Ejecutar desde la carpeta principal del proyecto:

```bash
python analisis_clima.py
```

## Análisis realizados

1. Registro del archivo CSV como vista virtual de DuckDB.
2. Limpieza de valores nulos y fechas inválidas.
3. Cálculo de temperaturas promedio por estación, año y mes.
4. Identificación de temperaturas máximas registradas por estación.
5. Medición del tiempo de ejecución de las consultas.

## Hallazgos principales

En el dataset de ejemplo:

- Valencia registra una temperatura máxima de 22 °C.
- Madrid registra una temperatura máxima de 16 °C.
- Barcelona registra una temperatura máxima de 19 °C.
- Los valores nulos de temperatura se excluyen de los cálculos.

Estos máximos corresponden únicamente al período representado en el CSV, no a récords históricos reales.

## Rendimiento

El script mide los tiempos de ejecución mediante `time.perf_counter()`.

Los resultados dependen del equipo y deben registrarse después de ejecutar el análisis.

## Conclusión

DuckDB permite realizar consultas SQL directamente sobre archivos CSV, sin configurar un servidor de base de datos.

Esto simplifica el procesamiento y análisis exploratorio de datos estructurados.
