from YousefMusic.plugins.play.filters import command
from pyrogram import filters
from pyrogram.types import Message

from YousefMusic import app
from YousefMusic.core.call import Zoro
from YousefMusic.utils.database import is_music_playing, music_off
from YousefMusic.utils.decorators import AdminRightsCheck
from YousefMusic.utils.inline import close_markup
from config import BANNED_USERS
# 𝐃𝐞𝐩𝐥𝐨𝐲𝐞𝐝 ⛥ 𓏺 Yousef .Tele_https://t.me/Y_o_V───────


@app.on_message(command(["وقف", "قف"]) & ~BANNED_USERS)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    user_mention = message.from_user.mention if message.from_user else "المشـرف"
    await Zoro.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(user_mention), reply_markup=close_markup(_)
    )
