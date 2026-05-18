import pandas as pd
from sqlalchemy import text
from db_connection import engine

final_df = pd.read_csv("data/processed/final_reviews.csv")

boa_df = pd.read_csv("data/processed/bank_of_abyssinia_reviews_clean.csv")
cbe_df = pd.read_csv(
    "data/processed/commercial_bank_of_ethiopia_reviews_clean.csv")
dashen_df = pd.read_csv("data/processed/dashen_bank_reviews_clean.csv")

cbe_df["bank_name"] = "CBE"
boa_df["bank_name"] = "BOA"
dashen_df["bank_name"] = "Dashen"

cbe_df["app_name"] = "CBE Mobile"
boa_df["app_name"] = "BOA Mobile"
dashen_df["app_name"] = "Dashen Super App"

metadata_df = pd.concat(
    [cbe_df, boa_df, dashen_df],
    ignore_index=True
)

metadata_df = metadata_df[
    [
        "review_id",
        "rating",
        "date",
        "source",
        "bank_name",
        "app_name"
    ]
]

metadata_df = metadata_df.rename(columns={
    "date": "review_date"
})

merged_df = pd.merge(
    final_df,
    metadata_df,
    on="review_id",
    how="left"
)

banks = merged_df[
    ["bank_name", "app_name"]
].drop_duplicates()

with engine.connect() as connection:

    connection.execute(text("DELETE FROM reviews"))
    connection.execute(text("DELETE FROM banks"))
    connection.commit()

    for _, row in banks.iterrows():

        connection.execute(
            text("""
                INSERT INTO banks (bank_name, app_name)
                VALUES (:bank_name, :app_name)
            """),
            {
                "bank_name": row["bank_name"],
                "app_name": row["app_name"]
            }
        )

    connection.commit()

banks_df = pd.read_sql("SELECT * FROM banks", engine)

bank_map = dict(zip(banks_df["bank_name"], banks_df["bank_id"]))

merged_df["bank_id"] = merged_df["bank_name"].map(bank_map)

reviews = merged_df[
    [
        "bank_id",
        "review_text",
        "rating",
        "review_date",
        "sentiment_label",
        "sentiment_score",
        "identified_theme",
        "source"
    ]
]

reviews.to_sql(
    "reviews",
    engine,
    if_exists="append",
    index=False
)

print("Data inserted")
