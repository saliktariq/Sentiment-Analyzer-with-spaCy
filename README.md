Sentiment Analyzer with spaCy
This project utilizes the natural language processing capabilities of spaCy along with the SpacyTextBlob extension 
to perform sentiment analysis on text data, specifically reviews. The importance of this project lies in its ability 
to preprocess text data, removing stopwords and non-alphabetic characters, lemmatizing the text, and then determining 
the overall sentiment (Positive, Negative, Neutral) of individual reviews. This can be particularly useful for businesses 
and developers looking to gauge public sentiment on their products or services from online reviews.

Table of Contents

Installation
Usage


Installation:
To install and run this project locally, follow these steps:

Ensure you have Python installed on your system.

Clone the repository or download the source code.

Install the required dependencies:
pip install spacy spacytextblob pandas

Download the necessary spaCy model:
python -m spacy download en_core_web_sm

Usage:
To use this sentiment analyzer, follow these steps:

Prepare a dataset in CSV format with at least one column named reviews.text containing the text of the reviews.
Run the script with your dataset's filepath as input. For example:

python sentiment_analyzer.py --filepath 'path_to_your_file.csv'

The script will preprocess the reviews, analyze their sentiment, and print the results, 
including a few rows from the processed dataset and sentiment analysis for sample reviews.

Example Code

# Assuming the script is named sentiment_analyzer.py
if __name__ == "__main__":
    filepath = 'your_reviews_file.csv'
    analyzed_df = analyze_dataset_reviews(filepath)
    print(analyzed_df[['reviews.text', 'sentiment']].head())
