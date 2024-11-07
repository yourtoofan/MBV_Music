import asyncio
import importlib
from sys import argv
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from MBVMusic import LOGGER, app, userbot
from MBVMusic.core.call import Hotty
from MBVMusic.misc import sudo
from MBVMusic.plugins import ALL_MODULES
from MBVMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

from MBVMusic.plugins.tools.clone import restart_bots




async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("MBVMusic.plugins" + all_module)
    LOGGER("MBVMusic.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Hotty.start()
    try:
        await Hotty.stream_call("https://graph.org/file/e999c40cb700e7c684b75.mp4")
    except NoActiveGroupCall:
        LOGGER("MBVMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Hotty.decorators()
    LOGGER("MBVMusic").info(
        "ᴅʀᴏᴘ ʏᴏᴜʀ ɢɪʀʟꜰʀɪᴇɴᴅ'ꜱ ɴᴜᴍʙᴇʀ ᴀᴛ @MBV_NETWORK ᴊᴏɪɴ @MBV_Music_gbot , @BLACKMAMBA_HU_VRO ꜰᴏʀ ᴀɴʏ ɪꜱꜱᴜᴇꜱ"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("MBVMusic").info("Stopping MBV Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
