from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE_PATH = BASE_DIR / "cirno_web_search_agent.env"


# Settings
class Settings(BaseSettings):
    # mcp config
    mcp_url: str = ""
    # llm config
    llm_api_key: str = ""
    llm_model_name: str = ""
    llm_base_url: str = ""
    # Exa config
    exa_api_key: str = ""
    # a2a config
    a2a_host: str = ""
    a2a_port: int = 4001
    use_db_push_notifications: bool = False
    use_db_task_store: bool = False
    db_url: str = ""

    model_config = SettingsConfigDict(
        env_file=ENV_FILE_PATH,
        env_file_encoding="utf-8",
        extra="allow",
    )


settings = Settings()