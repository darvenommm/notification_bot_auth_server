from ipaddress import IPv4Address
from pydantic import Field, IPvAnyAddress
from pydantic_settings import BaseSettings as PydanticBaseSettings, SettingsConfigDict


class BaseSettings(PydanticBaseSettings):
    server_host: IPvAnyAddress = Field(IPv4Address("0.0.0.0"), alias="SERVER_HOST")
    server_port: int = Field(8000, alias="SERVER_PORT", ge=0, le=65535)

    database_host: IPvAnyAddress = Field(alias="DATABASE_HOST")
    database_port: int = Field(alias="DATABASE_PORT", ge=0, le=65535)
    database_name: str = Field(alias="DATABASE_NAME")
    database_username: str = Field(alias="DATABASE_USERNAME")
    database_password: str = Field(alias="DATABASE_PASSWORD")
    database_schema: str = Field("public", alias="DATABASE_SCHEMA")

    @property
    def database_connection_string(self) -> str:
        user_info = f"{self.database_username}:{self.database_password}"
        address_info = f"{self.database_host}:{self.database_port}"

        return f"postgresql+asyncpg://{user_info}@{address_info}/{self.database_name}"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


base_settings = BaseSettings()
