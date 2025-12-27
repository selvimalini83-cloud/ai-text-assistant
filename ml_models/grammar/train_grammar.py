import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

# Load dataset
data = pd.read_csv("grammar_dataset.csv")

X_text = data["input"]
y_text = data["target"]

# Vectorize text
vectorizer = TfidfVectorizer()
X_vectors = vectorizer.fit_transform(X_text)

# Train nearest neighbor model
model = NearestNeighbors(n_neighbors=1, metric="cosine")
model.fit(X_vectors)

# Save model
with open("grammar_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save vectorizer
with open("grammar_vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

# Save correct sentences
with open("grammar_targets.pkl", "wb") as f:
    pickle.dump(y_text.tolist(), f)

print("✅ Grammar correction model trained successfully")
