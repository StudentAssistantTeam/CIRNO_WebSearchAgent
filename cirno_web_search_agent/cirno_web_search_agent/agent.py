import logging
# langchain
from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_core.messages import SystemMessage, HumanMessage
# Project dependencies
from cirno_web_search_agent.config import settings
from cirno_web_search_agent.tools import web_search
from cirno_web_search_agent.prompt import agent_system_prompt

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

    # Agent initialization
    async def initialize(self):
        # Get llm tools from mcp
        tools = await self.mcp_client.get_tools()
        # Add web search tool
        tools.append(web_search)
        self.agent = create_agent(self.llm, tools)

    # Test invoke
    async def test_invoke(self, prompt: str):
        # Load Messages history
        messages = []
        messages.append(SystemMessage(agent_system_prompt))
        messages.append(HumanMessage(prompt))
        chat_history = {
            "messages": messages
        }
        # Invoke agent
        result = await self.agent.ainvoke(chat_history)
        return result
