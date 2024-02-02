import html
import os
import random
import random
import re
import time
import asyncio
import os
from requests import get
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_input_location

from BATT import lucmd9
from random import choice
from lucmd9.razan.resources.strings import *
from telethon import events
from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers import get_user_from_event, reply_id
from . import spamwatch
from telethon.utils import get_display_name
from ..helpers.utils import reply_id, _catutils, parse_pre, yaml_format, install_pip, get_user_from_event, _format
import random
import re
import time
import asyncio
import os
from datetime import datetime
from platform import python_version

from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from BATT import StartTime, lucmd9, JEPVERSION
from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
plugin_category = "utils"


@lucmd9.on(admin_cmd(pattern="اكس1(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1045489068:
        return await edit_or_reply(mention, f"**هذا امر المطور**")
        ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "**父[ Thebatman  ✓ ](t.me/angthon)父**"
Qrue_IMG = gvarstatus("ALIVE_PIC") or Config.A_PIC or random.choice(["https://telegra.ph/file/9239ecac00e968641c64e.mp4"])

