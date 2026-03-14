import trafilatura
from google.adk.agents import Agent

def scrape_article(url: str) -> str:
    """Scrapes a news article URL and returns the text content."""
    downloaded = trafilatura.fetch_url(url)
    text = trafilatura.extract(downloaded)
    if text is None:
        return "Could not extract article text from this URL."
    return text

extractor_agent = Agent(
    name="extractor_agent",
    model="gemini-2.5-flash",
    description="Extracts key claims, loaded words, and framing from a news article.",
    instruction="""
    You are an expert media analyst. When given a news article URL:
    1. Use the scrape_article tool to get the article text
    2. Extract the 3-5 most important claims
    3. Identify emotionally loaded or biased words
    4. Describe the overall framing of the article

    Respond in this exact format:
    CLAIMS:
    - claim 1
    - claim 2

    LOADED WORDS:
    - word 1
    - word 2

    FRAMING:
    - framing observation
    """,
    tools=[scrape_article],
)