import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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


def sentiment_distribution():
    fig, ax = plt.subplots()

    sns.countplot(
        data=df,
        x="bank_name",
        hue="sentiment_label",
        ax=ax
    )

    ax.set_title("Sentiment Distribution by Bank")

    return fig


def rating_distribution():
    fig, ax = plt.subplots()

    sns.boxplot(
        data=df,
        x="bank_name",
        y="rating",
        ax=ax
    )

    ax.set_title("Rating Distribution by Bank")

    return fig


def theme_frequency():
    fig, ax = plt.subplots()

    themes = df["identified_theme"].value_counts().head(10)

    sns.barplot(
        x=themes.values,
        y=themes.index,
        ax=ax
    )

    ax.set_title("Top Themes")

    return fig
