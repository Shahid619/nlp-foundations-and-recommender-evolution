# Build a robust text preprocessing pipeline that can clean noisy real-world text ...
# ...(tweets, YouTube comments, or product reviews).

import spacy
import re
import pandas as pd
import numpy as np

# only testing top 100 rows
df=pd.read_csv("emoji_test.csv" ,nrows=100)

# print(df.head())


# regex cleaning pipeline
def clean_data(data):
    data = re.sub(r"http\S+|www\S+", "", data)
    data = re.sub(r"@\w+|#\w+", "", data)
    data = re.sub(r"[^\w\s,.!?']", "", data)
    data = re.sub(r"\s+", " ", data).strip().lower()
    return data

# create a new column of clean data 
df["cleaned_text"] = df["text"].apply(clean_data)

# regex calller function to iterate overall several line 
def regex_clean_review(dataset):
    return [clean_data(sentence) for sentence in dataset]

# process data through regex pipeline
cleaned_data=regex_clean_review(df["text"])



# step :2 --> spacy pipeline
Model=spacy.load("en_core_web_sm")
cleaned_news=[Model(data) for data in cleaned_data]

for sentence in cleaned_news:
    # print([token.lemma_ for token in sentence if not token.is_stop])
    print([token.text for token in sentence if not token.is_stop and not token.is_punct])
    
# print(df.head())

# save cleaned with raw data in a new file 
df.to_csv("cleaned_full_dataset.csv", index=False)
