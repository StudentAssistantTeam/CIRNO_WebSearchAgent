import logging
from typing import List
import json
import asyncio
# Project dependencies
from cirno_web_search_agent.web_search_engine import WebSearchEngine
from cirno_web_search_agent.data_models import (
    WebSearchInput
)
from cirno_web_search_agent.prompt import (
    websearch_description,
    final_answer_description
)
# langchain
from langchain.tools import tool

logger = logging.getLogger("Tool")


# Web Search Tool
@tool("web_search",
      args_schema=WebSearchInput,
      description=websearch_description
      )
async def web_search(query: List[str]):
    logger.info("Start web searching")
    # Web searching engine
    search_engine = WebSearchEngine()
    # Start searching
    results = await search_engine.search(query)
    summaries = []
    # Process results
    for result in results:
        tmp = {}
        summary = json.loads(result.summary)
        tmp["url"] = summary["url"]
        tmp["summary"] = summary["summary"]
        tmp["title"] = summary["title"]
        summaries.append(tmp)
    # Return
    return "# Info you get from the internet\n" + "".join(
        [
            f"\n## {item["title"]}\n### URL\n{item["url"]}\n### Summary\n{item["summary"]}\n"
            for idx, item in enumerate(summaries)
        ]
    )


# Get final answer.
@tool("final_answer", description=final_answer_description)
async def final_answer() -> None:
    return None


if __name__ == "__main__":
    try:
        print(asyncio.get_event_loop().run_until_complete(web_search(["The CEO of OpenAI"])))
    except Exception as e:
        print(e)
