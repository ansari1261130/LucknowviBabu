import re
import os
import pandas as pd
from indicnlp.tokenize import indic_tokenize
from unicodedata import normalize
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

RAW_DATA_PATH = os.path.join("data", "raw", "awadhi_book.txt")
CLEANED_DATA_PATH = os.path.join("data", "cleaned_awadhi.csv")

def clean_text(text):
    """Clean Awadhi text by removing unwanted symbols and normalizing."""
    text = normalize("NFKC", text)
    text = re.sub(r"[A-Za-z0-9]", "", text)
    text = re.sub(r"[!@#$%^&*()_+=\[\]{};:'\"|\\,.<>/?~`]", "", text)
    text = re.sub(r"[\U00010000-\U0010ffff]", "", text)  # Remove emojis
    text = re.sub(r"\s+", " ", text).strip()
    return text

def tokenize_text(text):
    """Tokenize Awadhi text into words."""
    return indic_tokenize.trivial_tokenize(text)

def preprocess_awadhi_data():
    """Main preprocessing pipeline."""
    if not os.path.exists(RAW_DATA_PATH):
        logging.error("Raw data file not found.")
        return

    with open(RAW_DATA_PATH, "r", encoding="utf-8") as f:
        raw_data = f.read()

    logging.info("Raw data loaded. Cleaning and tokenizing...")

    cleaned_text = clean_text(raw_data)
    tokens = tokenize_text(cleaned_text)

    df = pd.DataFrame({
        "original_text": [raw_data],
        "cleaned_text": [cleaned_text],
        "tokens": [" ".join(tokens)]
    })

    df.to_csv(CLEANED_DATA_PATH, index=False, encoding="utf-8")
    logging.info(f"Preprocessed data saved to {CLEANED_DATA_PATH}")

if __name__ == "__main__":
    preprocess_awadhi_data()
