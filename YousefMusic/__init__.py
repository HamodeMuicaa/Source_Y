from YousefMusic.core.bot import Zoro
from YousefMusic.core.dir import dirr
from YousefMusic.core.git import git
from YousefMusic.core.userbot import Userbot
from YousefMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Zoro()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()


# 𝐃𝐞𝐩𝐥𝐨𝐲𝐞𝐝 ⛥ 𓏺 Yousef .tele_https://t.me/y_o_v
