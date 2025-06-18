"""Simple web search wrapper using DuckDuckGo."""

from duckduckgo_search import DDGS


def search_web(query: str, max_results: int = 3) -> str:
    """Return a short snippet of web search results for *query*."""
    results = []
    try:
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=max_results):
                results.append(r.get("body", ""))
    except Exception:
        return ""
    return " \n".join(results)
