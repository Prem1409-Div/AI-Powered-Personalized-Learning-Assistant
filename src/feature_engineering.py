from sklearn.preprocessing import LabelEncoder

def encode_categorical(df, columns):
    le = LabelEncoder()
    for col in columns:
        df[col] = le.fit_transform(df[col].astype(str))
    return df
