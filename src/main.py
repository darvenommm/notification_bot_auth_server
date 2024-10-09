from sys import path
from pathlib import Path

current_dir = Path(__file__).resolve().parent
path.append(str(current_dir))
path.append(str(current_dir.parent))

import asyncio
import uvloop

loop_police = uvloop.EventLoopPolicy()
asyncio.set_event_loop_policy(loop_police)

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from settings.base import base_settings
from routes.users import user_router


def run_server() -> FastAPI:
    server = FastAPI(
        docs_url="/swagger",
        default_response_class=ORJSONResponse,
    )

    server.include_router(user_router)

    return server


if __name__ == "__main__":
    uvicorn.run(
        "src.main:run_server",
        host=str(base_settings.server_host),
        port=base_settings.server_port,
        factory=True,
    )
