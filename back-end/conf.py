from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    secret_data: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


conf = Config()
