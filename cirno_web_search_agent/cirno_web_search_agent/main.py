import logging
# a2a dependencies
from a2a.types import (
    AgentSkill
)
# project dependencies
import cirno_web_search_agent.logger_config as logger_config
from cirno_web_search_agent.prompt import (
    data_commons_skill_description
)

# logger
logger = logging.getLogger("server")


def main():
    # Data commons skill
    skill_data_commons = AgentSkill(
        id="data_commons_searching",
        name="Data Commons Searching",
        description=data_commons_skill_description,
        tags=["information", "data"],
        examples=[
            "Find me the GDP of all countries",
            "What is the solar energy consumption around the world?"
        ]
    )


# Run server
def run():
    logger_config.setup_logging()
    logger.info("Starting server")
    main()


if __name__ == "__main__":
    run()
