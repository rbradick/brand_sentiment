import os
os.environ["STREAMLIT_HOME"] = "/tmp"
os.environ["STREAMLIT_TELEMETRY_ENABLED"] = "0"

import os
os.environ["STREAMLIT_SUPPRESS_CONFIG_WARNINGS"] = "true"
os.environ["STREAMLIT_DISABLE_LOGGING"] = "1"
os.environ["STREAMLIT_HOME"] = "/tmp"
os.environ["STREAMLIT_TELEMETRY_ENABLED"] = "0"

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
