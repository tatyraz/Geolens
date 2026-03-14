import trafilatura
from dotenv import load_dotenv
import os
from agents.extractor import run_extractor
from agents.bias_classifier import run_bias_classifier
from agents.perspective import run_perspective
from agents.scorer import run_scorer
from agents.rewriter import run_rewriter

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def scrape_article(url):
    downloaded = trafilatura.fetch_url(url)
    text = trafilatura.extract(downloaded)
    if text is None:
        return "Could not extract article. Please paste the text manually."
    return text

def run_pipeline(url):
    print("\n🔗 Scraping article...")
    article = scrape_article(url)

    print("🔍 Running Extraction Agent...")
    extraction = run_extractor(article, GEMINI_API_KEY)

    print("⚖️ Running Bias Classifier Agent...")
    bias = run_bias_classifier(extraction, GEMINI_API_KEY)

    print("🌍 Running Perspective Agent...")
    perspective = run_perspective(article, bias, GEMINI_API_KEY)

    print("📊 Running Scoring Agent...")
    score = run_scorer(extraction, bias, perspective, GEMINI_API_KEY)

    print("📝 Running Rewriter Agent...")
    rewrite = run_rewriter(article, bias, perspective, GEMINI_API_KEY)

    print("\n" + "="*50)
    print("📰 NARRATIVEIQ ANALYSIS COMPLETE")
    print("="*50)
    print("\n🔍 EXTRACTION:\n", extraction)
    print("\n⚖️ BIAS:\n", bias)
    print("\n🌍 PERSPECTIVES:\n", perspective)
    print("\n📊 SCORE:\n", score)
    print("\n📝 NEUTRAL REWRITE:\n", rewrite)

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Russia%E2%80%93Ukraine_war"
    run_pipeline(url)