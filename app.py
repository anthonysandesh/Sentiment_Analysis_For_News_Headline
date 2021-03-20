import streamlit as st
import os
from git import Repo
import pickle
if(os.path.isdir("Sentiment-Analysis-Major-Project")):
  print("repo exists")
else:
  Repo.clone_from("https://github.com/kvora125/Sentiment-Analysis-Major-Project", "/content/Sentiment-Analysis-Major-Project")
sentiment_model=pickle.load(open('/content/Sentiment-Analysis-Major-Project/sentiment_model.p','rb'))
st.title("News Headline Sentiment Analysis")
st.subheader('This project is based on Vader sentiment Analysis(lexicon approach) with TFIFD Vectorizer and SVM to predict sentiment in news healdline')
st.write('This project uses data Web Scraped from inshorts.com and dataset built using prediction by vader sentiment analysis')
message = st.text_area("Enter News Headline","")
if st.button("Predict"):
  st.title(sentiment_model.predict([message])[0])