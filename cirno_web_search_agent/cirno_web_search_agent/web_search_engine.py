import logging
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
