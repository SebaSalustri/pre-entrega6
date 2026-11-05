
import duckdb
import time

# Conexión a DuckDB en memoria
con = duckdb.connect()

# Registrar el CSV como vista virtual
con.execute("""
    CREATE VIEW clima AS
    SELECT
        TRY_CAST(fecha AS DATE) AS fecha,
        estacion,
        TRY_CAST(temperatura AS DOUBLE) AS temperatura
    FROM read_csv(
    'C:/Users/usuario/Desktop/data science 2/tp6/analisis-clima-duckdb/datos/clima.csv',
    delim=',',
    header=true,
    columns={
        'fecha': 'VARCHAR',
        'estacion': 'VARCHAR',
        'temperatura': 'VARCHAR'
    }
)
""")

# Limpiar registros sin temperatura o fecha
con.execute("""
    CREATE VIEW clima_limpio AS
    SELECT *
    FROM clima
    WHERE temperatura IS NOT NULL
      AND fecha IS NOT NULL
""")

# Consulta 1: Promedios mensuales
inicio = time.perf_counter()

promedios = con.execute("""
    SELECT
        estacion,
        YEAR(fecha) AS anio,
        MONTH(fecha) AS mes,
        ROUND(AVG(temperatura), 2) AS promedio
    FROM clima_limpio
    GROUP BY estacion, anio, mes
    ORDER BY estacion, anio, mes
""").df()

tiempo_promedios = time.perf_counter() - inicio

print("PROMEDIOS MENSUALES")
print(promedios)
print(f"Tiempo: {tiempo_promedios:.6f} segundos")

# Consulta 2: Temperatura máxima por estación
inicio = time.perf_counter()

maximos = con.execute("""
    SELECT
        estacion,
        MAX(temperatura) AS temperatura_maxima
    FROM clima_limpio
    GROUP BY estacion
    ORDER BY temperatura_maxima DESC
""").df()

tiempo_maximos = time.perf_counter() - inicio

print("\nTEMPERATURAS MÁXIMAS")
print(maximos)
print(f"Tiempo: {tiempo_maximos:.6f} segundos")

con.close()
