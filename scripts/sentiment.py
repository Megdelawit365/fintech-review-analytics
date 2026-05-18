from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")


def sentiment_analysis(df):

    labels = []
    scores = []

    for text in df["review"].astype(str).tolist():
        result = sentiment_pipeline(text[:512])[0]
        labels.append(result["label"])
        scores.append(result["score"])

    df["transformer_sentiment_label"] = labels
    df["transformer_sentiment_score"] = scores

    return df
