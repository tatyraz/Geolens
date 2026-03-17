import streamlit as st
from dotenv import load_dotenv
import os
import sys
import trafilatura

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def scrape_article(url):
    downloaded = trafilatura.fetch_url(url)
    text = trafilatura.extract(downloaded)
    if text is None:
        return "Could not extract article text from this URL."
    return text

def analyze_article(url):
    from google import genai
    client = genai.Client(api_key=GEMINI_API_KEY)
    
    article = scrape_article(url)
    if "Could not extract" in article:
        return article
    
    prompt = f"""
    You are GeoLens, an expert media bias detection system.
    Analyze this news article and provide a COMPLETE analysis.

    You MUST always include ALL of these sections:

    🔍 KEY CLAIMS & FRAMING
    - List 3-5 key claims
    - List loaded/biased words
    - Describe the overall framing

    ⚖️ BIAS DETECTED
    - List bias types found
    - State overall bias direction
    - Rate severity: Low/Medium/High

    🌍 MISSING PERSPECTIVES
    - List missing voices or sides
    - List missing context

    📊 NEUTRALITY SCORE: [X]/100
    - Language bias: Low/Medium/High
    - Perspective bias: Low/Medium/High
    - Framing bias: Low/Medium/High
    - Source bias: Low/Medium/High
    - One sentence verdict

    📝 NEUTRAL REWRITE
    - Rewrite in neutral language (max 150 words)

    Article:
    {article}
    """
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

st.set_page_config(page_title="GeoLens", page_icon="🌍", layout="wide")

st.title("🌍 GeoLens")
st.subheader("AI-powered geopolitical bias detector")

tab1, tab2 = st.tabs(["Single Article", "Compare Two Articles"])

with tab1:
    url = st.text_input("Paste a news article URL:", placeholder="https://...")
    if st.button("🔍 Analyze", key="single"):
        if url:
            with st.spinner("Analyzing article..."):
                result = analyze_article(url)
            st.success("✅ Analysis complete!")
            st.markdown(result)
        else:
            st.warning("Please enter a URL first!")

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        url1 = st.text_input("Article 1 URL:", placeholder="https://...")
    with col2:
        url2 = st.text_input("Article 2 URL:", placeholder="https://...")
    
    if st.button("⚡ Compare", key="compare"):
        if url1 and url2:
            with st.spinner("Analyzing both articles..."):
                from google import genai
                client = genai.Client(api_key=GEMINI_API_KEY)
                
                article1 = scrape_article(url1)
                article2 = scrape_article(url2)
                
                prompt = f"""
                Compare these two news articles for bias:

                ARTICLE 1:
                {article1}

                ARTICLE 2:
                {article2}

                Provide:
                ⚖️ BIAS COMPARISON
                - Article 1 neutrality score: X/100
                - Article 2 neutrality score: X/100
                - Which is more biased and why
                - What narrative each outlet is pushing

                📝 COMBINED NEUTRAL SUMMARY
                - Write a neutral summary combining both articles
                """
                
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )
            st.success("✅ Comparison complete!")
            st.markdown(response.text)
        else:
            st.warning("Please enter both URLs!")