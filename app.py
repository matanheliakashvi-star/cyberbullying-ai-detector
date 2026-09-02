import streamlit as st
import joblib
import re

# Load trained model and TF-IDF vectorizer
model = joblib.load("cyberbullying_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")


# Clean text
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


# Page
st.set_page_config(
    page_title="Cyberbullying AI Detector",
    page_icon="🛡️"
)

st.title("🛡️ Cyberbullying AI Detector")

st.write(
    "Enter a social media comment below and the AI will "
    "classify it into a cyberbullying category."
)

# Input
tweet = st.text_area(
    "Enter a comment:",
    placeholder="Type a comment here..."
)

# Button
if st.button("🔍 Detect Cyberbullying"):

    if not tweet.strip():
        st.warning("Please enter a comment.")

    else:
        cleaned = clean_text(tweet)
        vector = vectorizer.transform([cleaned])

        prediction = model.predict(vector)[0]
        confidence = max(model.predict_proba(vector)[0]) * 100

        st.divider()

        if prediction == "not_cyberbullying":
            st.success("✅ NOT CYBERBULLYING")
        else:
            st.error("⚠️ CYBERBULLYING DETECTED")

        st.write(f"**Category:** {prediction}")
        st.write(f"**Confidence:** {confidence:.2f}%")
