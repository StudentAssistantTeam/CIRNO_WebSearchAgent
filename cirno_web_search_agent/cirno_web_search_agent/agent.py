import logging
# langchain
from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
# Project dependencies
from cirno_web_search_agent.config import settings

logger = logging.getLogger("agent")


# Agent
class Agent:
    def __init__(self):
        # Base llm
        self.llm = ChatOpenAI(
            model=settings.llm_model_name,
            api_key=settings.llm_api_key,
            base_url=settings.llm_base_url
        )
        # MCP client
        self.mcp_client = MultiServerMCPClient(
            {
                "data_commons": {
                    "url": settings.mcp_url,
                    "transport": "streamable-http"
                }
            }
        )
        # Agent
        self.agent = None

    async def initialize(self):
        # Get llm tools
        tools = await self.mcp_client.get_tools()
        self.agent = create_agent(self.llm, tools)
