import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
data = pd.read_csv("spam_dataset.csv")

X_text = data["sms"]
y = data["label"]

# Vectorize
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X_text)

# Train model
model = MultinomialNB()
model.fit(X, y)

# Save model
with open("spam_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save vectorizer
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)


print("✅ Training completed successfully")
