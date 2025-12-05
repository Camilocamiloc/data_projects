import streamlit as st
from src.inference import load_model, predict_sentiment
from streamlit_star_rating import st_star_rating

st.title("👍👎 Analizador de Sentimiento con IA")

# Cargar modelo una vez
classifier = load_model()

user_input = st.text_area("Escribe un texto para analizar (el modelo te dará una calificación según el comentario)")

if st.button("Analizar Sentimiento"):
    if user_input.strip() != "":
        result = predict_sentiment(user_input, classifier)
        label = result[0]['label']  # ejemplo: "2 stars"
        score = round(result[0]['score'], 3)

        # Extraer número de estrellas de la etiqueta (asumiendo formato "X stars")
        stars_count = int(label.split()[0])

        st.success(f"Sentimiento detectado: **{label}** (confianza: {score})")

        # Mostrar estrellas en modo lectura
        st_star_rating(label="Calificación", maxValue=5, defaultValue=stars_count, read_only=True)
    else:
        st.warning("Por favor ingresa un texto.")
