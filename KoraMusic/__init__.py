#
# Copyright (C) 2021-2022 by TeamKora@Github, < https://github.com/TeamKora >.
#
# This file is part of < https://github.com/TeamKora/KoraMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamKora/KoraMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from KoraMusic.core.bot import KoraBot
from KoraMusic.core.dir import dirr
from KoraMusic.core.git import git
from KoraMusic.core.userbot import Userbot
from KoraMusic.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = KoraBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
