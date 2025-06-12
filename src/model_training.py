from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pickle

def train_regression(X, y):
    model = RandomForestRegressor()
    model.fit(X, y)
    return model

def train_classification(X, y):
    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)
    return model

def train_clustering(X):
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(X)
    score = silhouette_score(X, kmeans.labels_)
    return kmeans, score

def save_model(model, path):
    with open(path, "wb") as f
