from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional
from crawl4ai import AsyncWebCrawler, CacheMode
from crawl4ai.async_configs import CrawlerRunConfig

app = FastAPI()

class HtmlInput(BaseModel):
    html: str

async def convert_html_to_markdown(html: str) -> str:
    raw_html_url = f"raw:{html}"
    config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=raw_html_url, config=config)
        if result.success:
            return result.markdown
        else:
            raise ValueError(f"Failed to convert HTML to Markdown: {result.error_message}")

@app.post("/html2markdown")
async def html2markdown(input: HtmlInput):
    markdown = await convert_html_to_markdown(input.html)
    return {"markdown": markdown}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3002)