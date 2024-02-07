import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import pandas as pd

# Load spaCy model and add SpacyTextBlob to the pipeline
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

# Function to preprocess text data
def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.lemma_.lower().strip() for token in doc if not token.is_stop and token.is_alpha]
    return ' '.join(tokens)

# Function to predict sentiment of a review
def predict_sentiment(review):
    doc = nlp(review)
    polarity = doc._.blob.polarity
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Load dataset from CSV
def load_data(filepath):
    return pd.read_csv(filepath)

# Apply preprocessing and sentiment analysis on the dataset
def analyze_dataset_reviews(filepath):
    df = load_data(filepath)
    # Ensure 'reviews.text' column exists
    if 'reviews.text' in df.columns:
        # Preprocess and predict sentiment
        df['processed_reviews'] = df['reviews.text'].apply(preprocess_text)
        df['sentiment'] = df['processed_reviews'].apply(predict_sentiment)
        return df
    else:
        raise ValueError("Dataset does not contain 'reviews.text' column.")

# Example usage
if __name__ == "__main__":
    filepath = 'amazon_product_reviews.csv'
    try:
        analyzed_df = analyze_dataset_reviews(filepath)
        print(analyzed_df[['reviews.text', 'sentiment']].head())  # Display first few rows of analysis
        
        # Test with sample reviews
        sample_reviews = [
            "This product was amazing and I loved it!",
            "I didn't like the product. It was awful and a waste of money.",
            "It's okay, but I'm not sure I would buy it again."
        ]
        for review in sample_reviews:
            sentiment = predict_sentiment(review)
            print(f"Review: {review}\nSentiment: {sentiment}\n")
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except ValueError as e:
        print(e)
