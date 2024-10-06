from YousefMusic.plugins.play.filters import command
from pyrogram import filters
from pyrogram.types import Message

from YousefMusic import app
from YousefMusic.core.call import Zoro
from YousefMusic.utils.database import set_loop
from YousefMusic.utils.decorators import AdminRightsCheck
from YousefMusic.utils.inline import close_markup
from config import BANNED_USERS
# 𝐃𝐞𝐩𝐥𝐨𝐲𝐞𝐝 ⛥ 𓏺 Yousef .Tele_https://t.me/Y_o_V───

#comand
@app.on_message(
    command(["/stop", "اسكت", "انهاء", "ايقاف"]) & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return
    await Zoro.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    user_mention = message.from_user.mention if message.from_user else "المشـرف"
    await message.reply_text(
        _["admin_5"].format(user_mention), reply_markup=close_markup(_)
    )
