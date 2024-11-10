from strings import get_string
from MBVMusic.misc import SUDOERS
from MBVMusic.utils.database import get_lang, is_maintenance
from config import SUPPORT_CHAT  # Ensure SUPPORT_CHAT is defined in config or replace with appropriate URL

def language(mystic):
    async def wrapper(_, message, **kwargs):
        # Check for maintenance mode
        if await is_maintenance():
            if message.from_user.id not in SUDOERS:
                return await message.reply_text(
                    text=f"The bot is currently under maintenance. Visit <a href='{SUPPORT_CHAT}'>support chat</a> for details.",
                    disable_web_page_preview=True,
                )
        try:
            await message.delete()
        except Exception as e:
            print(f"Error deleting message: {e}")

        # Set language
        try:
            language = await get_lang(message.chat.id)
            language = get_string(language)
        except Exception as e:
            print(f"Error retrieving language: {e}")
            language = get_string("en")
        return await mystic(_, message, language)

    return wrapper


def languageCB(mystic):
    async def wrapper(_, CallbackQuery, **kwargs):
        # Check for maintenance mode
        if await is_maintenance():
            if CallbackQuery.from_user.id not in SUDOERS:
                return await CallbackQuery.answer(
                    f"The bot is currently under maintenance. Visit support chat for more information.",
                    show_alert=True,
                )
        # Set language
        try:
            language = await get_lang(CallbackQuery.message.chat.id)
            language = get_string(language)
        except Exception as e:
            print(f"Error retrieving language: {e}")
            language = get_string("en")
        return await mystic(_, CallbackQuery, language)

    return wrapper


def LanguageStart(mystic):
    async def wrapper(_, message, **kwargs):
        # Set language
        try:
            language = await get_lang(message.chat.id)
            language = get_string(language)
        except Exception as e:
            print(f"Error retrieving language: {e}")
            language = get_string("en")
        return await mystic(_, message, language)

    return wrapper
