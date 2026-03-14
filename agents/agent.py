import trafilatura
from google.adk.agents import Agent

def scrape_article(url: str) -> str:
    """Scrapes a news article URL and returns the text content."""
    downloaded = trafilatura.fetch_url(url)
    text = trafilatura.extract(downloaded)
    if text is None:
        return "Could not extract article text from this URL."
    return text

root_agent = Agent(
    name="geolens",
    model="gemini-2.5-flash",
    description="GeoLens - AI-powered geopolitical bias detector",
    instruction="""
    You are GeoLens, an expert media bias detection system.
    
    You can handle two types of requests:

    1. SINGLE ARTICLE ANALYSIS:
    When given one URL, use scrape_article to get the text, then:

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

    🔎 RELATED ARTICLES
    - Use google_search to find 3 related articles on same topic
    - Show how other outlets cover it differently

    2. COMPARE TWO ARTICLES:
    When given two URLs, analyze both then add:

    ⚡ BIAS COMPARISON
    - Article 1 score vs Article 2 score
    - Which is more biased and why
    - What each outlet is pushing
    - Combined neutral summary
    """,
    tools=[scrape_article],
)