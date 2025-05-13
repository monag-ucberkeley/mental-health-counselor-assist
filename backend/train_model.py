import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

# Load data
df = pd.read_csv("mental_health_responses.csv")  # Make sure it has 'text' and 'label' columns
df.dropna(inplace=True)

# Binary classification: "direct" (1) or "indirect" (0)
df['label'] = df['response_type'].map({'direct': 1, 'indirect': 0})

# Create pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english', max_features=5000)),
    ('clf', LogisticRegression())
])

# Train
pipeline.fit(df['text'], df['label'])

# Save model
joblib.dump(pipeline, 'response_type_model.pkl')
print("Model saved to response_type_model.pkl")
