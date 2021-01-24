"""
Freyr - A Free stock API
Run Hypercon ASGI Web Server - https://gitlab.com/pgjones/hypercorn
"""
from hypercorn.config import Config
from hypercorn.asyncio import serve
import asyncio

from freyr import app

asyncio.run(serve(app, Config()))
