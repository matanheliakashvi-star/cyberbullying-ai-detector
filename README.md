<img width="1319" height="679" alt="Screenshot 2026-09-07 at 2 15 07 AM" src="https://github.com/user-attachments/assets/7efa56df-75c2-417e-913e-f8be0ba2500f" />
<img width="1329" height="679" alt="Screenshot 2026-09-07 at 2 14 33 AM" src="https://github.com/user-attachments/assets/f8624481-9ca0-49db-b268-f0a6708bd6f9" />

# 🛡️ Cyberbullying AI Detector

An AI-based cyberbullying detection system that uses Natural Language Processing (NLP) and Machine Learning to classify social media text.

## 📌 Project Overview

Cyberbullying is a serious problem on social media platforms. This project uses machine learning to analyze tweets and identify different types of cyberbullying.

The model classifies tweets into six categories:

- Age
- Ethnicity
- Gender
- Religion
- Other Cyberbullying
- Not Cyberbullying

## 🤖 Machine Learning Approach

The project uses:

- **TF-IDF (Term Frequency-Inverse Document Frequency)** for converting text into numerical features.
- **Logistic Regression** for text classification.
- Text preprocessing to clean tweets before classification.

### Workflow

```text
Tweet
  ↓
Text Cleaning
  ↓
TF-IDF Vectorization
  ↓
Logistic Regression
  ↓
Cyberbullying Category
