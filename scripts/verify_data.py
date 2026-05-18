import pandas as pd
from db_connection import engine

query1 = """
SELECT b.bank_name, COUNT(*) AS total_reviews
FROM reviews r
JOIN banks b
ON r.bank_id = b.bank_id
GROUP BY b.bank_name
"""

query2 = """
SELECT b.bank_name, AVG(r.rating) AS average_rating
FROM reviews r
JOIN banks b
ON r.bank_id = b.bank_id
GROUP BY b.bank_name
"""

query3 = """
SELECT *
FROM reviews
WHERE review_text IS NULL
OR sentiment_label IS NULL
OR identified_theme IS NULL
"""

reviews_per_bank = pd.read_sql(query1, engine)

average_rating = pd.read_sql(query2, engine)

nulls = pd.read_sql(query3, engine)

print(reviews_per_bank)

print(average_rating)

print(nulls)
