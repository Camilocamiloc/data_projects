from transformers import pipeline

def load_model():
    # Forzar uso de CPU con device=-1 para evitar error de meta tensor
    classifier = pipeline(
        "sentiment-analysis",
        model="nlptown/bert-base-multilingual-uncased-sentiment",
        device=-1
    )
    return classifier

def predict_sentiment(text, classifier):
    # pipeline ya devuelve lista de diccionarios con 'label' y 'score'
    return classifier(text)
