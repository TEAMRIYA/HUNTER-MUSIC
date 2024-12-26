from JioSavaan.core.bot import Anony
from JioSavaan.core.dir import dirr
from JioSavaan.core.git import git
from JioSavaan.core.userbot import Userbot
from JioSavaan.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
