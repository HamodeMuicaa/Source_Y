from pyrogram.enums import ParseMode

from YousefMusic import app
from YousefMusic.utils.database import is_on_off
from config import LOGGER_ID


────# 𝐃𝐞𝐩𝐥𝐨𝐲𝐞𝐝 ⛥ 𓏺 Yousef .Tele_https://t.me/Y_o_V─────

async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""━━━━ılıı◁ ❚ ɢꝛᴏᴜᴘ ❚  ▷ıılı━━━━
<b>╭⦿<b>{app.mention}
<b>╰⦿ ᴘʟᴧʏ ⸢ɢꝛᴏᴜᴘ⸥ ᴍᴜsɪᴄ♪</b>

<b>╭⦿ ᴄʜᴧᴛ ɴᴧᴍᴇ :</b> {message.chat.title}
<b>│᚜⦿ᴄʜᴧᴛ ᴜsᴇꝛ :</b> @{message.chat.username}
<b>│᚜⦿ɴᴧᴍᴇ :</b> {message.from_user.mention}
<b>╰⦿ ᴜsᴇꝛɴᴧᴍᴇ :</b> @{message.from_user.username}

<b>╭⦿ ǫᴜᴇꝛʏ :</b> {message.text.split(None, 1)[1]}
<b>╰⦿ sᴛꝛᴇᴧᴍᴛʏᴘᴇ :</b> {streamtype}
━ılıılıılıılıılıılıılıılıılıılıılıılılıılıılıılıılıılıılıılı━"""
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
