from pydantic import BaseModel, Field
from typing import List
# project dependencies
from cirno_web_search_agent.prompt import (
    keywords_definition
)

# Web search tool schema
class WebSearchInput(BaseModel):
    query: List[str] = Field(
        description=keywords_definition
    )