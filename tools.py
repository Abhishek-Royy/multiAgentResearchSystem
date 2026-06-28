    
from langchain.tools import tool
from bs4 import BeautifulSoup
from tavily import TavilyClient 
import requests
import os
from dotenv import load_dotenv
from rich import print

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


# Search query API implementation for research purpose, like Google scholar
@tool
def web_search(query: str) -> str:
    """
    Search the web for recent and reliable information on a topic.
    Returns titles, URLs, and snippets.
    """

    results = tavily.search(query=query, max_results=3)

    out = []

    for r in results["results"]:
        out.append(
            f"Title: {r['title']}\n"
            f"URL: {r['url']}\n"
            f"Snippet: {r['content'][:300]}\n"
        )

    return "\n" + "-" * 60 + "\n".join(out)


# print(web_search.invoke("What are the recent news of AI?"))


# For Scraping the URL and extract the data
@tool
def scrape_url(url:str)->str:
    """Scrape and return clean text content from given url for deeper reading."""

    try:
        response=requests.get(url,timeout=8,headers={"User-Agent":"Mozilla/5.0"})
        soup=BeautifulSoup(response.text,"html.parser")
        for tag in soup(["script","style","nav","footer"]):
            tag.decompose()
        return soup.get_text(separator=" ",strip=True)[:3000]
    except Exception as e:
        return f"Could not scrape URL:{str(e)}"
    
# print(scrape_url.invoke("https://www.nbcnews.com/tech/tech-news/michael-caine-ai-narration-homer-odyssey-audiobook-elevenlabs-rcna351469"))