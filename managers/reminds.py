import asyncio
from datetime import datetime

from db import User
from handlers.markups import *
import utils.custom_logger as cl

async def remindsManager():
    while True:
        try:
            cl.log("Reminds Manager", "debug", f"### Remind manager new cycle | Current datetime - {datetime.now()} ###")

            await asyncio.sleep(30)
        except Exception as ex:
            cl.log("Reminds Manager", "error", ex)
            await asyncio.sleep(30)