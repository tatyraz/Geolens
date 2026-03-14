import trafilatura
from googlesearch import search

def search_related_articles(query: str) -> str:
    """Searches for related news articles on the same topic."""
    try:
        results = []
        for url in search(query + " news", num_results=3):
            downloaded = trafilatura.fetch_url(url)
            text = trafilatura.extract(downloaded)
            if text:
                results.append(f"SOURCE: {url}\nSUMMARY: {text[:200]}...\n")
        
        if not results:
            return "No related articles found."
        
        return "\n".join(results)
    except Exception as e:
        return f"Search failed: {str(e)}"