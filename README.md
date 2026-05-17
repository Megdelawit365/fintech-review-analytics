## Project Overview
### Task 1: Data Collection and Preprocessing
- google-play-scraper library was used to collect reviews, ratings, dates, and app names for all three banks.
- Duplicate and missing values were handled and dates were normalized
- Cleaned data set was saved

### Task-2: Sentiment and Thematic Analysis
- Used a transformer model to classify review sentiment (positive/negative) with confidence scores.
- Aggregated sentiment by bank and star rating for comparison.
- Extracted keywords using TF-IDF to identify common topics in reviews.
- Grouped keywords into 3–5 business themes per bank (e.g., Account Issues, Performance, UI/UX).
- Analyzed sentiment by theme 
- Saved final dataset with sentiment labels, scores, and themes.

