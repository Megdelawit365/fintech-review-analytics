from google_play_scraper import app, reviews, Sort
import pandas as pd


def get_info(app_id, name):
    app_info = app(
        app_id,
        lang='en',
        country='et'
    )

    print("=" * 50)
    print(f"{name} App Info")
    print("=" * 50)
    print(f"App Title    : {app_info['title']}")
    print(f"Current Score: {app_info['score']}")
    print(f"Total Ratings: {app_info['ratings']:,}")
    print(f"Total Reviews: {app_info['reviews']:,}")
    print(f"Installs     : {app_info['installs']}")


def scrap(id):
    result, continuation_token = reviews(
        id,
        lang='en',
        country='et',
        sort=Sort.NEWEST,
        count=500,
        filter_score_with=None
    )

    print(f"Collected {len(result)} raw reviews")
    return result


def extract_columns(result, name):
    raw_data = []

    for r in result:
        raw_data.append({
            'review_id': r.get('reviewId', ''),
            'review': r.get('content', ''),
            'rating': r.get('score', None),
            'date': r.get('at', None),
            'bank': name,
            'source': 'Google Play'
        })

    df_raw = pd.DataFrame(raw_data)
    return df_raw
