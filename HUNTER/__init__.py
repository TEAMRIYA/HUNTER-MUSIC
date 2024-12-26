from HUNTER.core.bot import Anony
from HUNTER.core.dir import dirr
from HUNTER.core.git import git
from HUNTER.core.userbot import Userbot
from HUNTER.misc import dbb, heroku

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
