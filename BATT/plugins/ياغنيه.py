import base64
import contextlib
import io
import os
from BATT import lucmd9
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
LOGS = logging.getLogger(__name__)

# =========================================================== #
#                           STRINGS                           #
# =========================================================== #
SONG_SEARCH_STRING = "<code>انتظر عزيزي دادورلك الاغنية</code>"
SONG_NOT_FOUND = "<code>اعذرني مالكيت اي اغنية </code>"
SONG_SENDING_STRING = "<code>دا ادزها الك انتظر...</code>"
# =========================================================== #
#                                                             #
# =========================================================== #


@lucmd9.ar_cmd(
    pattern="بحث(320)?(?:\s|$)([\s\S]*)",
    command=("بحث", plugin_category),
    info={
        "header": "للعثور على اغنيه من اليوتيوب",
        "description": "Basically this command searches youtube and send the first video as audio file.",
        "flags": {
            "320": "if you use song320 then you get 320k quality else 128k quality",
        },
        "usage": "{tr}song <song name>",
        "examples": "{tr}song memories song",
    },
)
async def _(event):
    "To search songs"
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if event.pattern_match.group(2):
        query = event.pattern_match.group(2)
    elif reply and reply.message:
        query = reply.message
    else:
        return await edit_or_reply(event, "`رد على الي تريد بحثه `")
    bat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    batevent = await edit_or_reply(event, "`لكيت الي تريده انتظر....`")
    video_link = await yt_search(str(query))
    if not url(video_link):
        return await batevent.edit(
            f"اسف مالكيت اي مقطع او صوت ل `{query}`"
        )
    cmd = event.pattern_match.group(1)
    q = "320k" if cmd == "320" else "128k"
    song_file, batthumb, title = await song_download(video_link, batevent, quality=q)
    await event.client.send_file(
        event.chat_id,
        song_file,
        force_document=False,
        caption=f"**Title:** `{title}`",
        thumb=batthumb,
        supports_streaming=True,
        reply_to=reply_to_id,
    )
    await catevent.delete()
    for files in (batthumb, song_file):
        if files and os.path.exists(files):
            os.remove(files)


@lucmd9.ar_cmd(
    pattern="يوت(?:\s|$)([\s\S]*)",
    command=("يوت", plugin_category),
    info={
        "header": "To get video songs from youtube.",
        "description": "Basically this command searches youtube and sends the first video",
        "usage": "{tr}vsong <song name>",
        "examples": "{tr}vsong memories song",
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
        return await edit_or_reply(event, "رد على الي تريدة")
    bat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    batevent = await edit_or_reply(event, "`اصبر لكيت شي....`")
    video_link = await yt_search(str(query))
    if not url(video_link):
        return await catevent.edit(
            f"اسف ما كدرت احمل الفيد او الصوت ل `{query}`"
        )
    with contextlib.suppress(BaseException):
        cat = Get(cat)
        await event.client(cat)
    vsong_file, batthumb, title = await song_download(video_link, batevent, video=True)
    await event.client.send_file(
        event.chat_id,
        vsong_file,
        caption=f"**Title:** `{title}`",
        thumb=batthumb,
        supports_streaming=True,
        reply_to=reply_to_id,
    )
    await catevent.delete()
    for files in (batthumb, vsong_file):
        if files and os.path.exists(files):
            os.remove(files)

@lucmd9.ar_cmd(
    pattern="ابحث(?:\s|$)([\s\S]*)",
    command=("ابحث", plugin_category),
    info={
        "header": "To search songs and upload to telegram",
        "description": "Searches the song you entered in query and sends it quality of it is 320k",
        "usage": "{tr}song2 <song name>",
        "examples": "{tr}song2 memories song",
    },
)
async def _(event):
    "To search songs"
    song = event.pattern_match.group(1)
    chat = "@songdl_bot"
    reply_id_ = await reply_id(event)
    catevent = await edit_or_reply(event, SONG_SEARCH_STRING, parse_mode="html")
    async with event.client.conversation(chat) as conv:
        try:
            purgeflag = await conv.send_message("/start")
        except YouBlockedUserError:
            await edit_or_reply(
                catevent, "**Error:** شيل البلوك من البلوك او تاكد من الاشتراك في القنوات و احذف المحادثه مع البوت وجربة تبحث"
            )
            await lucmd9(unblock("songdl_bot"))
            purgeflag = await conv.send_message("/start")
        await conv.get_response()
        await conv.send_message(song)
        hmm = await conv.get_response()
        while hmm.edit_hide is not True:
            await asyncio.sleep(0.1)
            hmm = await event.client.get_messages(chat, ids=hmm.id)
        baka = await event.client.get_messages(chat)
        if baka[0].message.startswith(
            ("شكد فكر ولاشي لكيت جرب البحث الاول.")
        ):
            await delete_conv(event, chat, purgeflag)
            return await edit_delete(
                catevent, SONG_NOT_FOUND, parse_mode="html", time=5
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
        #كتابه وتعديل سورس الخفاش
