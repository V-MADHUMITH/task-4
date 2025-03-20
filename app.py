import joblib
vectorizer = joblib.load("tfidf_vectorizer.pkl")
model = joblib.load("spam_model.pkl")

print("Spam Detector is ready!")

while True:
    user_message = input("\nEnter a message to check (or type 'exit' to quit): ")
    
    if user_message.lower() == "exit":
        print("Exiting spam detector. Goodbye!")
        break
    message_tfidf = vectorizer.transform([user_message])
    prediction = model.predict(message_tfidf)
    print("Prediction:", "📩 Spam" if prediction[0] == 1 else "✅ Not Spam")
