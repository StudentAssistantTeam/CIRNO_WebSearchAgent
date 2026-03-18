import logging
import asyncio
from typing import List
# Project dependency
from cirno_web_search_agent.config import settings
from cirno_web_search_agent.prompt import (
    websearch_return_schema
)
# Exa dependency
from exa_py import AsyncExa

logger = logging.getLogger("Web Search Engine")


# Web Search Engine
class WebSearchEngine():
    def __init__(self):
        self.exa = AsyncExa(
            api_key=settings.exa_api_key
        )
        # Schema
        self.schema = websearch_return_schema

    # Search
    async def search(self, keywords: List[str]):
        # Process query
        query = " ".join(keywords)
        # Get result
        results = await self.exa.search(
            query=query,
            type="deep",
            contents = {
                "summary": {
                    "query": "Give your summary",
                    "schema": self.schema
                },
                "text": True
            },
            num_results=5
        )
        return results.results


if __name__ == "__main__":
    engine = WebSearchEngine()
    print(asyncio.get_event_loop().run_until_complete(engine.search(["technology", "news", "climate"])))
