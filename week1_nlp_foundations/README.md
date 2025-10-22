Task 1 — Text Preprocessing Pipeline
🎯 Objective

Build a robust text preprocessing pipeline to clean noisy, real-world text data such as tweets, YouTube comments, or product reviews.
The goal is to prepare clean text suitable for further NLP tasks like sentiment analysis or classification.

📁 Dataset

The input dataset is a CSV file containing:

Column	Description
text	Raw text data (e.g., tweets, comments)
label	Numerical label or class associated with each text


Dependencies:

pip install pandas spacy numpy
python -m spacy download en_core_web_sm
