import streamlit as st
from scraper.google_news import scrape_google_news
from sentiment.analyzer import analyze_sentiment
import pandas as pd

st.title("🧠 Brand Sentiment Analysis App")
brand = st.text_input("Enter a brand name to analyze", "Nike")

if st.button("Run Analysis"):
    st.write("🔍 Scraping data...")
    articles = scrape_google_news(brand)

    if articles:
        st.write(f"✅ {len(articles)} articles found.")
        df = analyze_sentiment(articles)
        st.dataframe(df)
    else:
        st.warning("No articles found. Try another brand.")