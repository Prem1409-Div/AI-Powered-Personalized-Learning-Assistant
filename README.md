# AI-Powered Personalized Learning Assistant

## Overview
Personalized AI assistant for students to predict scores, detect dropout risk, summarize lessons, and generate quizzes.

## Features
- Logistic Regression for pass/fail prediction
- Random Forest for score prediction
- KMeans for learning style clustering
- Transformers for summarization and quiz generation

## personalized-learning-assistant/
│
├── data/
│   ├── raw/              # Raw dataset files
│   ├── processed/        # Cleaned & preprocessed datasets
│
├── models/
│   ├── ml_models/        # Saved models (Pickle, .pt, etc.)
│   ├── llm_outputs/      # Summarized topics, quizzes, etc.
│
├── notebooks/
│   ├── EDA.ipynb
│   ├── ML_Models.ipynb
│   ├── LLM_Integration.ipynb
│
├── src/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   ├── quiz_generator.py
│   ├── summary_generator.py
│
├── app/
│   ├── streamlit_app.py
│
├── requirements.txt
├── README.md


## How to Run
```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```
