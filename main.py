import nltk
nltk.download('punkt')
nltk.download('vader_lexicon')
nltk.download('averaged_perceptron_tagger')
nltk.download('brown')

from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

# Function to perform text analysis
def analyze_text():
    # Get input text from the user
    text = input("Enter the text you want to analyse: ")
    
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Calculate word frequency
    word_freq = FreqDist(tokens)
    
    # Perform sentiment analysis
    sentiment_analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = sentiment_analyzer.polarity_scores(text)
    
    # Perform rhetorical criticism
    blob = TextBlob(text)
    parts_of_speech = blob.tags
    
    # Perform interaction analysis
    interaction_words = ["you", "your", "yours"]
    interaction_count = sum(word.lower() in interaction_words for word in tokens)
    
    # Perform performance studies analysis
    performance_words = ["act", "perform", "stage"]
    performance_count = sum(word.lower() in performance_words for word in tokens)
    
    # Perform descriptive analysis
    word_count = len(tokens)
    
    # Perform exploratory analysis
    unique_words = set(tokens)
    unique_word_count = len(unique_words)
    
    # Perform inferential analysis
    average_word_length = sum(len(word) for word in tokens) / word_count
    
    # Perform predictive analysis
    first_word = tokens[0] if tokens else None
    
    # Perform causal analysis
    last_word = tokens[-1] if tokens else None
    
    # Perform mechanistic analysis
    character_count = len(text)
    
    # Print word frequency
    print("Word Frequency:")
    for word, freq in word_freq.most_common(10):
        print(word, "-", freq)
    
    # Print sentiment analysis results
    print("\nSentiment Analysis:")
    print("Positive:", sentiment_scores['pos'])
    print("Negative:", sentiment_scores['neg'])
    print("Neutral:", sentiment_scores['neu'])
    print("Compound:", sentiment_scores['compound'])
    
    # Print rhetorical criticism results
    print("\nRhetorical Criticism:")
    for word, pos in parts_of_speech:
        if pos.startswith('JJ'):
            print(word, "- Adjective")
        elif pos.startswith('VB'):
            print(word, "- Verb")
    
    # Print interaction analysis result
    print("\nInteraction Analysis:")
    print("Number of interaction words:", interaction_count)
    
    # Print performance studies analysis result
    print("\nPerformance Studies Analysis:")
    print("Number of performance words:", performance_count)
    
    # Print descriptive analysis result
    print("\nDescriptive Analysis:")
    print("Word count:", word_count)
    
    # Print exploratory analysis result
    print("\nExploratory Analysis:")
    print("Unique word count:", unique_word_count)
    
    # Print inferential analysis result
    print("\nInferential Analysis:")
    print("Average word length:", average_word_length)
    
    # Print predictive analysis result
    print("\nPredictive Analysis:")
    print("First word:", first_word)
    
    # Print causal analysis result
    print("\nCausal Analysis:")
    print("Last word:", last_word)
    
    # Print mechanistic analysis result
    print("\nMechanistic Analysis:")
    print("Character count:", character_count)

# Call the analysis function
analyze_text()




