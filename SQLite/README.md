# Prueba Técnica – SQL

## Objetivo
Evaluar la capacidad de extraer, manipular y analizar datos mediante SQL, sobre un modelo relacional.

---

## Enfoque de la solución

La información entregada originalmente en Excel fue replicada en una base de datos **SQLite** (`prueba_sql.db`) para simular un entorno SQL real.  
Las consultas fueron ejecutadas desde un **Jupyter Notebook**, permitiendo mostrar tanto las queries como sus resultados y, cuando es útil, visualizaciones exploratorias.

---

## Contenido

- `prueba_sql.db`  
  Base de datos SQLite con las tablas:
  `creditos`, `personas`, `municipios`, `departamentos`, `almacenes`.

- `prueba.ipynb`  
  Notebook con:
  - Definición del esquema relacional
  - Ejecución de las consultas SQL solicitadas
  - Visualización de resultados como dataframes
  - Gráficas exploratorias para análisis rápido

---

## Consultas desarrolladas

1. **JOINs básicos**  
   Valor total facturado por almacén y municipio.

2. **Agregaciones**  
   Promedio de facturación y sumatorias de saldos por departamento.

3. **CTEs y subconsultas**  
   Identificación del departamento con mayor valor facturado.

4. **Análisis de riesgo**  
   Top 5 almacenes con mayor porcentaje de créditos de alto riesgo.

5. **Análisis temporal**  
   Evolución mensual del valor facturado por departamento.

6. **Bajo rendimiento**  
   Almacenes con facturación consistentemente por debajo del promedio de su departamento.

---

## Ejecución

Requisitos:
```bash
pip install pandas
