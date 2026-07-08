from langchain_core.tools import tool
from tavily import TavilyClient
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import os

load_dotenv(override=True)


def get_tavily_client():
    tavily_key = os.getenv("TAVILY_API_KEY")

    if not tavily_key:
        raise ValueError("TAVILY_API_KEY not found. Please add it in your .env file.")

    return TavilyClient(api_key=tavily_key)


@tool
def web_search(query: str) -> str:
    """
    Search the web for recent and reliable information.
    Returns titles, URLs, and snippets.
    """

    tavily = get_tavily_client()

    results = tavily.search(
        query=query,
        max_results=5,
        search_depth="advanced"
    )

    output = []

    for result in results.get("results", []):
        title = result.get("title", "No title")
        url = result.get("url", "No URL")
        content = result.get("content", "No snippet available")

        output.append(
            f"Title: {title}\n"
            f"URL: {url}\n"
            f"Snippet: {content[:500]}\n"
        )

    if not output:
        return "No search results found."

    return "\n-----\n".join(output)


@tool
def scrape_url(url: str) -> str:
    """
    Scrape clean text content from a given URL for deeper reading.
    """

    try:
        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()

        text = soup.get_text(separator=" ", strip=True)

        if not text:
            return "No readable text found on this page."

        return text[:4000]

    except Exception as e:
        return f"Could not scrape URL: {str(e)}"


if __name__ == "__main__":
    print(web_search.invoke("Generative AI latest news"))
    print(scrape_url.invoke("https://www.ibm.com/topics/generative-ai"))