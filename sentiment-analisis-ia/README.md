## 👍👎 Analizador de Sentimientos con Transformers y Streamlit

Aplicación para analizar sentimiento (1–5 estrellas) usando el modelo nlptown/bert-base-multilingual-uncased-sentiment de Hugging Face. Incluye interfaz web sencilla con Streamlit y módulo para procesar archivos CSV (análisis de sentimientos de comentarios múltiples).

#### 🚀 Funcionalidades

Análisis de sentimiento basado en estrellas.

Interfaz web con Streamlit.

Webscrapping de los comentarios de la aplicación en google play.

Visualización con estrellas (streamlit-star-rating).

Procesamiento masivo de comentarios en CSV.

#### 📦 Instalación
pip install -r requirements.txt

Dependencias principales:

streamlit
transformers
torch
pandas
streamlit-star-rating

#### ▶️ Uso
Aplicación web
streamlit run app.py

Procesar un CSV

En processed_csv.py, ajusta:

procesar_csv("ruta_archivo.csv", "columna_texto")


Luego ejecuta:

python src/processed_csv.py


Genera resultados.csv con:

comentario

sentimiento (1–5 estrellas)

confianza

#### 📁 Estructura
app.py
src/
 ├─ inference.py
 └─ processed_csv.py
