import pandas as pd

def load_dataset(path):
    df = pd.read_csv(path)
    if 'prompt' not in df.columns or 'question' not in df.columns:
        raise ValueError("CSV must contain 'prompt' and 'question' columns")
    return df