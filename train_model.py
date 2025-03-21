import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

df = pd.read_csv("spam.csv", encoding="latin-1")[["v1", "v2"]]
df.columns = ["label", "message"]
df["label"] = df["label"].map({"ham": 0, "spam": 1})
X_train, X_test, y_train, y_test = train_test_split(df["message"], df["label"], test_size=0.2, random_state=42)
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)
y_pred = model.predict(X_test_tfidf)
print("Model Accuracy:", accuracy_score(y_test, y_pred))
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")
joblib.dump(model, "spam_model.pkl")

print("Training complete! Model saved as 'spam_model.pkl'.")
