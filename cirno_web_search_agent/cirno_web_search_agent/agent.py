import logging
import asyncio
# langchain
from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_core.messages import SystemMessage, HumanMessage
# Project dependencies
from cirno_web_search_agent.config import settings
from cirno_web_search_agent.tools import web_search, final_answer
from cirno_web_search_agent.prompt import agent_system_prompt
from cirno_web_search_agent.data_models import StreamingMessage
import cirno_web_search_agent.logger_config as logger_config

logger = logging.getLogger("agent")


# Agent
class agent:
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
        tools.append(final_answer)
        self.agent = create_agent(self.llm, tools)
        logger.info("Agent initialization finished")

    # Test invoke
    async def test_invoke(self, prompt: str):
        logger.info("Start testing")
        # Load Messages history
        messages = []
        messages.append(SystemMessage(content=agent_system_prompt))
        messages.append(HumanMessage(content=prompt))
        chat_history = {
            "messages": messages
        }
        # Invoke agent
        result = await self.agent.ainvoke(chat_history)
        return result

    # Streaming
    async def streaming(self, prompt: str, context_id: str):
        logger.info("Start streaming")
        try:
            # Configuration
            config = {'configurable': {'thread_id': context_id}}
            # Settting messages
            messages = []
            messages.append(SystemMessage(content=agent_system_prompt))
            messages.append(HumanMessage(content=prompt))
            chat_history = {
                "messages": messages
            }
            # Response record
            response_record = []
            async for chunk in self.agent.astream(chat_history):
                for step, data in chunk.items():
                    if step=="model":
                        response_record.append(data['messages'][0].content)
                    yield StreamingMessage(
                        step=step,
                        content=data['messages'][0].content,
                        done=False
                    )
            yield StreamingMessage(
                step="finish",
                content=response_record[len(response_record)-1],
                done=True
            )
        except Exception as e:
            # Error handling
            logger.error(f"Error occurred while streaming: {e}")
            yield StreamingMessage(
                step="error",
                content=f"Sorry, I have encountered an error {e}",
                done=True
            )


if __name__ == "__main__":
    logger_config.setup_logging()
    Agent = agent()
    asyncio.run(Agent.initialize())
    iterer = Agent.streaming(prompt="Find me info about GDP of the countries", context_id="114514")


    async def itering():
        async for i in iterer:
            if (i.step == "model" or i.step == "finish"):
                print(i.done)
                print(i.content)


    asyncio.run(itering())

