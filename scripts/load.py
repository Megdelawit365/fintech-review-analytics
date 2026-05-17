import pandas as pd


def load_files():
    df_abyssinia = pd.read_csv(
        "../data/processed/bank_of_abyssinia_reviews_clean.csv")
    df_cbe = pd.read_csv(
        "../data/processed/commercial_bank_of_ethiopia_reviews_clean.csv")
    df_dashen = pd.read_csv("../data/processed/dashen_bank_reviews_clean.csv")

    return {
        "abyssinia": df_abyssinia,
        "cbe": df_cbe,
        "dashen": df_dashen
    }
