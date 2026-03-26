import logging
import httpx
import uvicorn
# a2a dependencies
from a2a.types import (
    AgentSkill,
    AgentCapabilities,
    AgentCard
)
from a2a.server.apps import A2AStarletteApplication
from a2a.server.tasks import (
    InMemoryPushNotificationConfigStore,
    InMemoryTaskStore,
    DatabasePushNotificationConfigStore,
    DatabaseTaskStore,
    BasePushNotificationSender
)
from a2a.server.request_handlers import DefaultRequestHandler
# project dependencies
import cirno_web_search_agent.logger_config as logger_config
from cirno_web_search_agent.prompt import (
    data_commons_skill_description,
    web_search_skill_description,
    agent_description
)
from cirno_web_search_agent.config import settings
from cirno_web_search_agent.agent import SUPPORTED_CONTENT_TYPES
from cirno_web_search_agent.agent_executor import agent_executor

# logger
logger = logging.getLogger("server")


def main():
    # Skills
    data_commons_skill = AgentSkill(
        id="data_commons_searching",
        name="Data Commons Searching",
        description=data_commons_skill_description,
        tags=["information", "data"],
        examples=[
            "Find me the GDP of all countries",
            "What is the solar energy consumption around the world?"
        ]
    )
    web_search_skill = AgentSkill(
        id="web_search",
        name="Web Search",
        description=web_search_skill_description,
        tags=["information", "web"],
        examples=[
            "Find me the definition of GDP."
        ]
    )
    # Agent capabilities
    capabilities = AgentCapabilities(
        streaming=True
    )
    # Agent Card
    agent_card = AgentCard(
        name="Web Search & Data Collection Agent",
        description=agent_description,
        url=f"http://{settings.a2a_host}:{settings.a2a_port}/",
        version="0.1.0",
        default_input_modes=SUPPORTED_CONTENT_TYPES,
        default_output_modes=SUPPORTED_CONTENT_TYPES,
        capabilities=capabilities,
        skills=[
            web_search_skill,
            data_commons_skill
        ]
    )
    # Server
    httpx_client = httpx.AsyncClient()
    # Configuring the push notification system
    if settings.use_db_push_notifications:
        push_config_store = DatabasePushNotificationConfigStore(
            settings.db_url
        )
    else:
        push_config_store = InMemoryPushNotificationConfigStore()
    push_sender = BasePushNotificationSender(
        httpx_client=httpx_client,
        config_store=push_config_store
    )
    # Configure the tasks store system
    if settings.use_db_task_store:
        task_store = DatabaseTaskStore(settings.db_url)
    else:
        task_store = InMemoryTaskStore()
    request_handler = DefaultRequestHandler(
        agent_executor=agent_executor(),
        task_store=task_store,
        push_config_store=push_config_store,
        push_sender=push_sender
    )
    # Server configuration
    server = A2AStarletteApplication(
        agent_card=agent_card,
        http_handler=request_handler
    )
    # Start the server
    uvicorn.run(
        server.build(),
        host=settings.a2a_host,
        port=settings.a2a_port
    )


# Run server
def run():
    logger_config.setup_logging()
    logger.info("Starting server")
    main()


if __name__ == "__main__":
    run()
