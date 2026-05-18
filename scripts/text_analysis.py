from sklearn.feature_extraction.text import TfidfVectorizer


def extract_keywords(df, text_col="clean_review", n=10):

    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        stop_words="english",
        min_df=2
    )

    X = vectorizer.fit_transform(df[text_col])
    keywords = vectorizer.get_feature_names_out()
    scores = X.sum(axis=0).A1

    top_keywords = sorted(
        zip(keywords, scores),
        key=lambda x: x[1],
        reverse=True
    )[:n]

    return top_keywords
