import pandas as pd
import joblib
from preprocess import clean_text  # Corrected import path

def load_model(model_path):
    """Load a trained model from a file."""
    try:
        return joblib.load(model_path)
    except FileNotFoundError:
        print(f"Error: Model file not found at {model_path}")
        return None

def load_vectorizer(vectorizer_path):
    """Load the vectorizer used during training."""
    try:
        return joblib.load(vectorizer_path)
    except FileNotFoundError:
        print(f"Error: Vectorizer file not found at {vectorizer_path}")
        return None

def predict_genre(model, description, vectorizer):
    """Predict the genre of a movie based on its description."""
    if model is None or vectorizer is None:
        return "Model or vectorizer not loaded."

    # Preprocess the text
    processed_text = clean_text(description)
    
    # Convert to numerical features using the vectorizer
    features = vectorizer.transform([processed_text])
    # print(features.shape)

    # Convert to DataFrame with correct feature names
    features_df = pd.DataFrame(features.toarray(), columns=vectorizer.get_feature_names_out())

    # Predict the genre
    prediction = model.predict(features_df)
    return prediction[0]


