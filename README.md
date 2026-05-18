# Fintech Review Analytics

Customer Experience Analytics for Fintech Apps

---

## Project Overview

This project analyzes Google Play Store reviews for three Ethiopian banks:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

It is part of the 10 Academy AI Mastery Week 2 Challenge, where the goal is to turn raw user reviews into useful business insights using data engineering and NLP techniques.

The project helps banks understand:
- What users like
- What users complain about
- What features they want

---

# Task 1: Data Collection and Preprocessing

- Google Play Store reviews were scraped and cleaned to produce a structured dataset suitable for analysis.
- Reviews were collected using the `google-play-scraper` library for three Ethiopian banks.
- The following cleaning steps were applied:
  - Duplicate reviews were removed using `review_id`
  - Rows with missing review text or rating were dropped
  - Review text was cleaned and standardized
  - Dates were converted to `YYYY-MM-DD` format
- The dataset was saved as CSV files in the `data/processed/` directory.

## Limitations

- Reviews may include multiple languages
- Older reviews may not be accessible

---

# Task 2: Sentiment and Thematic Analysis

## Sentiment Analysis

- Sentiment analysis and thematic extraction were performed to understand user opinions and identify recurring issues.
- A transformer-based model (`distilbert-base-uncased-finetuned-sst-2-english`) was used to classify each review into sentiment labels with confidence scores.
- Sentiment was aggregated by:
  - Bank
  - Star rating

## Thematic Analysis

- Keywords were extracted using TF-IDF and grouped into business-relevant themes such as:
  - Login issues
  - Transaction issues
  - Performance issues
  - UI/UX feedback
  - Other issues

- The final dataset was saved as `final_reviews.csv`.

## Key Observations

- Performance-related issues were frequent across all banks
- Login and authentication issues were commonly reported
- UI/UX feedback was generally more positive than functional issues

---

# Task 3: Data Storage in PostgreSQL

## Objective

Store cleaned and processed review data in a relational PostgreSQL database to simulate a real-world data engineering pipeline.

---

## Database Setup

- PostgreSQL was installed and configured locally.
- A database named `bank_reviews` was created.

---

## Database Schema

Two tables were created:

### banks

Stores metadata about each bank.

- bank_id (Primary Key)
- bank_name
- app_name

### reviews

Stores processed review data.

- review_id (Primary Key)
- bank_id (Foreign Key)
- review_text
- rating
- review_date
- sentiment_label
- sentiment_score
- identified_theme
- source

---

## Data Pipeline

- Cleaned dataset (`final_reviews.csv`) was merged with bank metadata from raw datasets.
- A modular Python pipeline using SQLAlchemy was used for database insertion.
- Data integrity was ensured using `review_id` as the unique identifier for merging datasets.
- Foreign key relationships were established between reviews and banks.

---

## Verification Queries

The following checks were performed:

- Count of reviews per bank
- Average rating per bank
- Null value checks on critical columns

---

## Key Outcomes

- PostgreSQL database successfully created and populated
- Both tables (`banks`, `reviews`) populated with review data
- Relational structure enables comparison across banks
- Data is now ready for advanced analysis and visualization in Task 4

---
# Project Structure

```bash
fintech-review-analytics/
│
├── .github/workflows/
│
├── data/
│   ├── raw/
│   └── processed/
│       └── final_reviews.csv
│
├── notebooks/
│   ├── web-scraping.ipynb
│   ├── sentiment-analysis.ipynb
│   ├── database.ipynb
│
├── scripts/
│   ├── scrap.py
│   ├── preprocess.py
│   ├── load.py
│   ├── sentiment.py
│   ├── theme.py
│   ├── text_analysis.py
│   ├── db_connection.py
│   ├── create_tables.py
│   ├── insert_data.py
│   └── verify_data.py
│
├── sql/
│   └── schema.sql
│
├── src/
├── tests/
├── requirements.txt
└── README.md
```

---

# Tools & Technologies

- Python
- pandas
- PostgreSQL
- SQLAlchemy
- scikit-learn (TF-IDF)
- Hugging Face Transformers
- google-play-scraper
- Matplotlib
- NLTK