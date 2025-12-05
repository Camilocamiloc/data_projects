import pandas as pd
from inference import load_model, predict_sentiment

classifier = load_model()

def procesar_csv(ruta_csv, columna_texto):
    df = pd.read_csv(ruta_csv)

    if columna_texto not in df.columns:
        raise ValueError(f"La columna '{columna_texto}' no existe en el CSV")

    resultados = []

    for texto in df[columna_texto].dropna():
        pred = predict_sentiment(texto, classifier)[0]
        resultados.append({
            'comentario': texto,
            'sentimiento': pred['label'],
            'confianza': round(pred['score'], 3)
        })

    return pd.DataFrame(resultados)

df_resultados = procesar_csv(r"C:\Users\boda1\Downloads\reviews_visionamos_filtrado.csv", "content")
df_resultados.to_csv("resultados.csv", index=False)
