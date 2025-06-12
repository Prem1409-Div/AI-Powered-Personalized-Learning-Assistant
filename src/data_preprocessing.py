import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    df = df.dropna()
    return df

def preprocess_for_model(df):
    df['time_sec'] = df['time_sec'].fillna(df['time_sec'].mean())
    return df
