from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from settings.base import base_settings

engine = create_async_engine(base_settings.database_connection_string, echo=True)

get_session = async_sessionmaker(bind=engine)
