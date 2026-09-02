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
