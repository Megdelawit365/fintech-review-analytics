import pandas as pd
import re


def clean_text(text):
    if pd.isna(text):
        return ""
    text = str(text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def preprocess_reviews(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    # 1. Drop missing
    df = df.dropna(subset=["review", "rating"])

    # 2. Remove duplicates
    if "review_id" in df.columns:
        df = df.drop_duplicates(subset=["review_id"])

    # 3. Clean text
    df["review"] = df["review"].apply(clean_text)
    df = df[df["review"].str.len() > 0]

    # 4. Validate ratings
    df = df[(df["rating"] >= 1) & (df["rating"] <= 5)]
    df["rating"] = df["rating"].astype(int)

    # 5. Normalize date
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"])
    df["date"] = df["date"].dt.strftime("%Y-%m-%d")

    return df
