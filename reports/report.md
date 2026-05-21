# Bank Reviews Sentiment Analysis Report

## 1. Introduction

This project analyzes customer reviews from three banking applications: BOA, CBE, and Dashen. The objective is to understand user sentiment, extract key themes, and generate actionable product and service recommendations based on real review data stored in a PostgreSQL database.

---

## 2. Data Overview

The dataset consists of structured review data with the following fields:

- bank_id
- bank_name
- review_text
- rating
- review_date
- sentiment_label
- sentiment_score
- identified_theme
- source

Data is stored in a relational PostgreSQL database with two tables:

- banks (bank metadata)
- reviews (user feedback data)

---

## 3. Data Quality Observation

A significant portion of reviews are categorized under the theme “Other”, indicating:

- Low specificity in user feedback
- Limited effectiveness of automated theme extraction
- Users often provide short or generic comments

This impacts fine-grained insight extraction.

---

## 4. Bank-Level Insights

### 4.1 BOA (Bank of Abyssinia)

**Sentiment Score:** 0.075 (Lowest)

**Average Rating:** 3.57

#### Drivers
- No strong identifiable drivers due to high proportion of generic feedback

#### Pain Points
- Account-related issues (low frequency but present)

#### Insight
BOA receives highly generic feedback, suggesting low engagement or limited feature-specific user reporting.

---

### 4.2 CBE

**Sentiment Score:** 0.367 (Highest)

**Average Rating:** 4.12 (Highest)

#### Drivers
- UI/UX improvements (16 mentions)

#### Pain Points
- Transaction issues (16 mentions)
- Performance issues (9 mentions)

#### Insight
CBE performs best overall but suffers from backend reliability and transaction stability issues.

---

### 4.3 Dashen Bank

**Sentiment Score:** 0.289

**Average Rating:** 3.93

#### Drivers
- UI/UX improvements (36 mentions)

#### Pain Points
- Transaction issues (14 mentions)
- Performance issues (10 mentions)

#### Insight
Dashen has strong user experience feedback but faces recurring performance and transaction reliability issues.

---

## 5. Cross-Bank Comparison

### Sentiment Ranking
1. CBE (Best)
2. Dashen
3. BOA (Worst)

### Rating Ranking
1. CBE (4.12)
2. Dashen (3.93)
3. BOA (3.57)

### Key Observation
- CBE leads in both sentiment and ratings
- BOA significantly underperforms in user satisfaction
- Dashen is mid-performing with strong UX perception but backend issues

---

## 6. Key Insights

- “Other” dominates most reviews, reducing theme granularity
- Transaction reliability is a shared pain point across all banks
- UI/UX improvements are the most positively perceived aspect
- Performance issues directly correlate with lower sentiment scores

---

## 7. Recommendations

### BOA
- Improve data categorization of customer feedback
- Investigate and fix account-related issues
- Increase feature clarity in mobile app

### CBE
- Fix transaction failure issues
- Improve backend performance stability
- Reduce system latency during peak usage

### Dashen
- Improve transaction reliability
- Optimize application performance under load
- Maintain strong UI/UX but enhance stability

---

## 8. Conclusion

The analysis shows that while CBE leads in overall user satisfaction, all banks share a common need for improved transaction stability and backend performance. UI/UX improvements positively influence sentiment, but system reliability remains the most critical factor affecting user experience.