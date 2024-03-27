#بيو
import base64
import contextlib
import io
import os
from telethon import types
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from validators.url import url

from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import delete_conv, yt_search
from ..helpers.tools import media_type
from ..helpers.utils import reply_id
from . import lucmd9, song_download

plugin_category = "utils"
LOGS = logging.getLogger(name)

# =========================================================== #
#                           STRINGS                           #
# =========================================================== #
SONG_SEARCH_STRING = "<code>صبر خلدور....</code>"
SONG_NOT_FOUND = "<code> !شكد فكر مالكيت شي</code>"
SONG_SENDING_STRING = "<code>لكيت الي تريده...</code>"
# =========================================================== #
#                                                             #
# =========================================================== #


@lucmd9.ar_cmd(
    pattern="بحث(320)?(?:\s|$)([\s\S]*)",
    command=("بحث", plugin_category),
    info={
        "header": "اغنيه من اليوت.",
        "description": "ياخذ اغنيه من يوت ويدزها الك.",
        "flags": {
            "320": "if you use song320 then you get 320k quality else 128k quality",
        },
        "usage": "{tr}بحث <song name>",
        "examples": "{tr}بحث memories song",
    },
)
async def _(event):
    "لبحث الاغنيه"
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if event.pattern_match.group(2):
        query = event.pattern_match.group(2)
    elif reply and reply.message:
        query = reply.message
    else:
        return await edit_or_reply(event, "رد على شي الي تريده ")
    bat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    batevent = await edit_or_reply(event, "لكيته....")
    video_link = await yt_search(str(query))
    if not url(video_link):
        return await catevent.edit(
            f"فكرر مالكيت شي`{query}`"
        )
    cmd = event.pattern_match.group(1)
    q = "320k" if cmd == "320" else "128k"
    song_file, catthumb, title = await song_download(video_link, batevent, quality=q)
    await event.client.send_file(
        event.chat_id,
        song_file,
        force_document=False,
        caption=f"Title: {title}",
        thumb=batthumb,
        supports_streaming=True,
        reply_to=reply_to_id,
    )
    await batevent.delete()
    for files in (batthumb, song_file):
        if files and os.path.exists(files):
            os.remove(files)

@lucmd9.ar_cmd(
    pattern="يوت(?:\s|$)([\s\S]*)",
    command=("يوت", plugin_category),
    info={
        "header": "فيد من يوت.",
        "description": "ياخذ اول فيد سيرج باليوت",
        "usage": "{tr}يوت <song name>",
        "examples": "{tr}يوت memories song",
    },
)
async def _(event):
    "To search video songs"
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
    elif reply and reply.message:
        query = reply.message
    else:
        return await edit_or_reply(event, "رد على الشي تريده")
    bat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    batevent = await edit_or_reply(event, "لكيتهاا....")
    video_link = await yt_search(str(query))
    if not url(video_link):
        return await batevent.edit(
            f"مالكيت شي اسف {query}"
        )
    with contextlib.suppress(BaseException):
        bat = Get(cat)
        await event.client(cat)
    vsong_file, batthumb, title = await song_download(video_link, catevent, video=True)
    await event.client.send_file(
        event.chat_id,
        vsong_file,
        caption=f"Title: {title}",
        thumb=batthumb,
        supports_streaming=True,
        reply_to=reply_to_id,
    )
    await batevent.delete()
    for files in (batthumb, vsong_file):
        if files and os.path.exists(files):
            os.remove(files)


@lucmd9.ar_cmd(
    pattern="ابحث(?:\s|$)([\s\S]*)",
    command=("ابحث", plugin_category),
    info={
        "header": "لبحث الاغاني من تلي",
        "description": "Searches the song you entered in query and sends it quality of it is 320k",
        "usage": "{tr}ابحث <song name>",
        "examples": "{tr}ابحث memories song",
    },
)
async def _(event):
    "To search songs"
    song = event.pattern_match.group(1)
    chat = "@songdl_bot"
    reply_id_ = await reply_id(event)
    batevent = await edit_or_reply(event, SONG_SEARCH_STRING, parse_mode="html")
    async with event.client.conversation(chat) as conv:
        try:
            purgeflag = await conv.send_message("/start")
        except YouBlockedUserError:
            await edit_or_reply(
                batevent, "Error: شيل البلوك من البوت او اشترك بالقنوات الاجباري بالبوت وامسح المحادثه انت والبوت وجرب
            await catub(unblock("songdl_bot"))
            purgeflag = await conv.send_message("/start")
        await conv.get_response()
        await conv.send_message(song)
        hmm = await conv.get_response()
        while hmm.edit_hide is not True:
            await asyncio.sleep(0.1)
            hmm = await event.client.get_messages(chat, ids=hmm.id)
        baka = await event.client.get_messages(chat)
        if baka[0].message.startswith(
            ("iam not find anything")
        ):
            await delete_conv(event, chat, purgeflag)
            return await edit_delete(
                batevent, SONG_NOT_FOUND, parse_mode="html", time=5
            )
        await batevent.edit(SONG_SENDING_STRING, parse_mode="html")
        await baka[0].click(0)
        await conv.get_response()
        await conv.get_response()
        music = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_file(
            event.chat_id,
            music,
            caption=f"<b>Title :- <code>{song}</code></b>",
            parse_mode="html",
            reply_to=reply_id_,
        )
        await batevent.delete()
        await delete_conv(event, chat, purgeflag)
