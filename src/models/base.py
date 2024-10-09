from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

from settings.base import base_settings


metadata = MetaData(schema=base_settings.database_schema)


class Base(DeclarativeBase):
    metadata = metadata
