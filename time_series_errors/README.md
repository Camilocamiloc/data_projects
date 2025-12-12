# Predicción de Errores para Entidades Financieras (Prophet + SARIMA + Dashboard)

Este proyecto realiza un análisis y predicción de errores transaccionales diarios por entidad a partir de datos históricos. Se utilizan dos modelos de series de tiempo:

- **Prophet** (Meta)
- **SARIMA** (Statsmodels)

Los resultados se visualizan en un **dashboard interactivo en Dash**, que permite explorar tanto los datos históricos como las predicciones generadas para cada entidad.




## + Estructura del proyecto

```

data/
└── agg_day.csv

product/
├── predicciones_prophet.csv
└── predicciones_sarima.csv

app.py
st_error_analysis.ipynb
README.md
requirements.txt

```

---

## + Instalación


###  Instalar dependencias

pip install -r requirements.txt

---

## + Generación de predicciones

Ejecutar el script de modelado:


python st_error_analysis.ipynb


Esto generará en la carpeta `product/`:

* `predicciones_prophet.csv`
* `predicciones_sarima.csv`

---

## + Ejecución del Dashboard

Iniciar el servidor:


python app.py




El dashboard incluye:

* Serie histórica
* Predicciones Prophet y SARIMA con bandas de confianza
* Tabla de los próximos 7 días
* Heatmap semanal histórico

---

## + Requisitos del dataset

El archivo `agg_day.csv` debe contener al menos:

| fecha      | entidad        | errores |
| ---------- | -------------- | ------- |
| 2024-01-01 | BancoMinería A | 15      |

---

## 🛠 Tecnologías usadas

* Python 3.9+
* Prophet
* Statsmodels (SARIMA)
* Dash & Plotly
* Pandas
* Seaborn & Matplotlib

