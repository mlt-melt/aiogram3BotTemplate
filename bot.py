import asyncio

from storage.config import dp, bot
from managers.reminds import remindsManager
import utils.custom_logger as cl

import admin_panel.admin.admin
import admin_panel.mailing.mailing

import handlers.start
import handlers.profile
import handlers.chat_join

async def bot_stopped():
    cl.log("Bot", "critical", f"Bot has been stopped")

async def main():
    tasks = [
        dp.start_polling(bot),
        remindsManager()
    ]
    dp.shutdown.register(bot_stopped)
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())