import pandas as pd
from scripts.db_connection import engine


df = pd.read_sql("""
SELECT 
    r.review_id,
    r.bank_id,
    b.bank_name,
    r.review_text,
    r.rating,
    r.review_date,
    r.sentiment_label,
    r.sentiment_score,
    r.identified_theme,
    r.source
FROM reviews r
JOIN banks b ON r.bank_id = b.bank_id
""", engine)


def bank_summary():
    sentiment = df.groupby("bank_name")["sentiment_score"].mean()
    rating = df.groupby("bank_name")["rating"].mean()
    return sentiment, rating


def drivers_and_pain_points():

    drivers = (
        df[df["sentiment_label"] == "POSITIVE"]
        .groupby(["bank_name", "identified_theme"])
        .size()
        .reset_index(name="count")
        .sort_values(["bank_name", "count"], ascending=False)
    )

    pains = (
        df[df["sentiment_label"] == "NEGATIVE"]
        .groupby(["bank_name", "identified_theme"])
        .size()
        .reset_index(name="count")
        .sort_values(["bank_name", "count"], ascending=False)
    )

    return drivers, pains
