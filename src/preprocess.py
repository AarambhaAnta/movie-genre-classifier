import re
import nltk
import string
import swifter
from multiprocessing import cpu_count
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Ensure necessary NLTK resources are available
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize stopwords and lemmatizer
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text: str) -> str:
    """
    Cleans input text by removing special characters, stopwords, and lemmatizing.
    
    Parameters:
        text (str): Input text string.
        
    Returns:
        str: Cleaned text.
    """
    if not isinstance(text, str):
        return ""

    # Convert to lowercase
    text = text.lower()

    # Remove special characters, punctuation, and digits
    text = re.sub(r'[^a-z\s]', '', text)

    # Tokenize text
    words = word_tokenize(text)

    # Remove stopwords
    words = [word for word in words if word not in stop_words]

    # Lemmatize words
    words = [lemmatizer.lemmatize(word) for word in words]

    return " ".join(words)

def clean_text_parallel(df, text_column, new_column_name):
    """
    Applies clean_text function to a dataframe column in parallel.
    
    Parameters:
        df (pd.DataFrame): Input dataframe.
        text_column (str): Name of the column to clean.
        
    Returns:
        pd.DataFrame: Dataframe with cleaned text.
    """
    df[new_column_name] = df[text_column].swifter.apply(clean_text).tolist()
    return df

# Example usage
if __name__ == "__main__":
    import pandas as pd
    
    sample_data = {
        "Description": [
            "This is an example sentence! It includes numbers 123 and special characters #@&.",
            "Another sample text, with punctuation & symbols like $ and %!",
            "Final example: Let's see how well this works?"
        ]
    }
    
    df = pd.DataFrame(sample_data)
    
    print("Before Cleaning:")   
    print(df.head())

    # Apply parallel cleaning
    df = clean_text_parallel(df, "Description")

    print("\nAfter Cleaning:")
    print(df.head())

