# Text Analysis Program

This llows users to perform various types of analysis on text input. It utilises the Natural Language Toolkit (NLTK) and the TextBlob library to provide insights into the provided text.

The program includes the following analysis features:

- Word Frequency: Calculates the frequency of words in the text and displays the top 10 most frequent words.
- Sentiment Analysis: Uses the VADER sentiment analysis tool to determine the positive, negative, neutral, and compound sentiment scores of the text.
- Rhetorical Criticism: Identifies and displays adjectives and verbs present in the text.
- Interaction Analysis: Counts the number of interaction words (e.g., "you", "your", "yours") in the text.
- Performance Studies Analysis: Counts the number of performance-related words (e.g., "act", "perform", "stage") in the text.
- Descriptive Analysis: Provides information about the word count in the text.
- Exploratory Analysis: Calculates the number of unique words in the text.
- Inferential Analysis: Computes the average word length in the text.
- Predictive Analysis: Displays the first word in the text.
- Causal Analysis: Shows the last word in the text.
- Mechanistic Analysis: Counts the number of characters in the text.


## Installation

1. Make sure you have Python 3.x installed on your system.
2. Install the required libraries by running the following commands in your terminal:
   
   pip install nltk
   pip install textblob
   
3. Download necessary NLTK data by running the following commands in Python:
   
   import nltk
   nltk.download('punkt')
   nltk.download('vader_lexicon')
   nltk.download('averaged_perceptron_tagger')
   nltk.download('brown')

