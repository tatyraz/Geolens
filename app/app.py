import streamlit as st
from dotenv import load_dotenv
import os
from main import run_pipeline, scrape_article
from agents.extractor import run_extractor
from agents.bias_classifier import run_bias_classifier
from agents.perspective import run_perspective
from agents.scorer import run_scorer
from agents.rewriter import run_rewriter

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

st.set_page_config(page_title="NarrativeIQ", page_icon="🗞️", layout="wide")

st.title(" 🌍 GeoLens")
st.subheader("AI-powered media bias detector")

url = st.text_input("Paste a news article URL here:", placeholder="https://...")

if st.button("🔍 Analyze"):
    if url:
        with st.spinner("Scraping article..."):
            article = scrape_article(url)

        with st.spinner("Running 5 AI agents..."):
            extraction = run_extractor(article, GEMINI_API_KEY)
            bias = run_bias_classifier(extraction, GEMINI_API_KEY)
            perspective = run_perspective(article, bias, GEMINI_API_KEY)
            score = run_scorer(extraction, bias, perspective, GEMINI_API_KEY)
            rewrite = run_rewriter(article, bias, perspective, GEMINI_API_KEY)

        st.success("✅ Analysis complete!")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🔍 Key Claims & Framing")
            st.write(extraction)

            st.markdown("### 🌍 Missing Perspectives")
            st.write(perspective)

        with col2:
            st.markdown("### ⚖️ Bias Analysis")
            st.write(bias)

            st.markdown("### 📊 Neutrality Score")
            st.write(score)

        st.markdown("### 📝 Neutral Rewrite")
        st.write(rewrite)
    else:
        st.warning("Please enter a URL first!")