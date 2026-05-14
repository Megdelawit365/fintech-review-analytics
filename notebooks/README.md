# Data Collection and Preprocessing  

These notebooks include google play store reviews for three apps: Commercial bank of Ethiopia, Bank of Abyssinia and Dashen Bank

## Scraping  
500 google reviews for each of the three apps were scraped using the google-play-scraper library. Each banking application was queried using its Google Play package ID to extract 5 fields: reviews, ratings, data, id and source(Google play).

## Date range
The dataset spans from the earliest available review on Google Play to the most recent reviews at the time of scraping (May 2026). No manual filtering by date was applied, and all available reviews returned by the scraper were included.

## Limitations
Multiple identical review contents were found for all applications. This might have an effect on results obtained later. 
