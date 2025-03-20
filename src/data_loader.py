import pandas as pd
import os

def load_data(file_path: str, is_train: bool = True):
    """
    Load dataset from a custom-formatted text file.
    
    Parameters:
        file_path (str): Path to the text file.
        is_train (bool): Whether the file is training data (contains genres).
        
    Returns:
        pd.DataFrame: Loaded dataset as a Pandas DataFrame.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        columns = ["ID", "Title", "Genre", "Description"] if is_train else ["ID", "Title", "Description"]
        
        df = pd.read_csv(file_path, sep=' ::: ', engine='python', names=columns)
        print(f"Data loaded successfully from {file_path}")
        print(f"Shape of dataset: {df.shape}")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Example usage (Uncomment below to test)
# train_df = load_data("data/raw/train_data.txt", is_train=True)
# test_df = load_data("data/raw/test_data.txt", is_train=False)
# print(train_df.head())
# print(test_df.head())

