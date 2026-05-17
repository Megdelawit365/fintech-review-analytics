from tqdm import tqdm


def sentiment_analysis(df_clean):
    try:
        from transformers import pipeline
        sent_model = pipeline(
            "sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

        transformer_results = []
        batch_size = 16
        for i in tqdm(range(0, len(df_clean), batch_size), desc="Running Transformer Sentiment"):
            batch = df_clean['review'].iloc[i:i + batch_size].tolist()
            preds = sent_model(batch)
            transformer_results.extend(preds)

        df_clean['transformer_sentiment_label'] = [p['label']
                                                   for p in transformer_results]
        df_clean['transformer_sentiment_score'] = [p['score'] if p['label']
                                                   == 'POSITIVE' else -p['score'] for p in transformer_results]

        print("\nTransformer Sentiment Distribution:")
        print(df_clean['transformer_sentiment_label'].value_counts(
            normalize=True).round(2))

    except Exception as e:
        print(f"Transformer skipped: {e}")
