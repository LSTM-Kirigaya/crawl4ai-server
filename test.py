import asyncio
from crawl4ai import AsyncWebCrawler, CacheMode
from crawl4ai.async_configs import CrawlerRunConfig

async def crawl_raw_html():
    raw_html = "<h1>Hello, World!</h1>"
    raw_html_url = f"raw:{raw_html}"
    config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)

    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=raw_html_url, config=config)
        if result.success:
            print("Markdown Content from Raw HTML:")
            print(result.markdown)
        else:
            print(f"Failed to crawl raw HTML: {result.error_message}")

asyncio.run(crawl_raw_html())
