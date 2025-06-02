# routes/websearch.py

from fastapi import APIRouter, Query
import requests
from bs4 import BeautifulSoup

router = APIRouter(prefix="/websearch", tags=["Web Search"])

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

@router.get("/")
async def web_search(q: str = Query(..., description="Search query")):
    try:
        url = f"https://www.bing.com/search?q={q.replace(' ', '+')}"
        response = requests.get(url, headers=HEADERS)

        soup = BeautifulSoup(response.text, "html.parser")
        results = []

        for item in soup.select(".b_algo")[:5]:  # Top 5 results
            title = item.select_one("h2")
            link = item.select_one("a")
            if title and link:
                results.append({
                    "title": title.get_text(strip=True),
                    "link": link["href"]
                })

        return {
            "query": q,
            "results": results
        }

    except Exception as e:
        return {"error": str(e)}
# routes/websearch.py

from fastapi import APIRouter, Query
import requests
from bs4 import BeautifulSoup

router = APIRouter(prefix="/websearch", tags=["Web Search"])

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

@router.get("/")
async def web_search(q: str = Query(..., description="Search query")):
    try:
        url = f"https://www.bing.com/search?q={q.replace(' ', '+')}"
        response = requests.get(url, headers=HEADERS)

        soup = BeautifulSoup(response.text, "html.parser")
        results = []

        for item in soup.select(".b_algo")[:5]:  # Top 5 results
            title = item.select_one("h2")
            link = item.select_one("a")
            if title and link:
                results.append({
                    "title": title.get_text(strip=True),
                    "link": link["href"]
                })

        return {
            "query": q,
            "results": results
        }

    except Exception as e:
        return {"error": str(e)}
