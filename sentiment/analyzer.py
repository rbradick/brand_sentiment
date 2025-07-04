from transformers import pipeline
import pandas as pd

sentiment_model = pipeline("sentiment-analysis")

def analyze_sentiment(texts):
    results = sentiment_model(texts)
    df = pd.DataFrame({
        "text": texts,
        "label": [r['label'] for r in results],
        "score": [r['score'] for r in results]
    })
    return df