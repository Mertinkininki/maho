from config import LOG, LOG_GROUP_ID
from YukkiMusic import app
from YukkiMusic.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Gizli Grubta"
        logger_text = f"""
**Log Bilgi**

**Sohbeti:** {message.chat.title} [`{message.chat.id}`]
**Kullanıcı:** {message.from_user.mention}
**Kullanıcı adı:** @{message.from_user.username}
**Kullanıcı Kimliği :** `{message.from_user.id}`
**Sohbet linki:** {chatusername}

**Sorgu:** {message.text}

**Akış Türü:** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
