import asyncio
import os
import time
from datetime import datetime
from pydub import AudioSegment
from pydub.silence import split_on_silence
from tinytag import TinyTag  # استيراد مكتبة tinytag

from BATT import lucmd9

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id
from . import progress, reply_id

plugin_category = "utils"

thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")


@lucmd9.ar_cmd(
    pattern="تسمية ?(-f)? ([\s\S]*)",
    command=("تسمية", plugin_category),
    info={
        "header": "To rename and upload the replied file.",
        "flags": {"f": "will upload as file that is document not streamable."},
        "description": "If flag is not used then will upload as steamable file",
        "usage": [
            "{tr}تسمية <اسم الملف الجديد>",
            "{tr}تسميه -f <اسم الملف الجديد>",
        ],
    },
)
async def _(event):
    "To rename and upload the file"
    thumb = thumb_image_path if os.path.exists(thumb_image_path) else None
    flags = event.pattern_match.group(1)
    forcedoc = bool(flags)
    supsstream = not flags
    batevent = await edit_or_reply(
        event,
        "`Rename & التحميل في الطريق ربما يستغرق وقتا طويلا حسب حجم الملف🦇",
    )
    reply_to_id = await reply_id(event)
    input_str = event.pattern_match.group(2)
    if not event.reply_to_msg_id:
        return await batevent.edit(
            "**Syntax : **`.rnup file name` as reply to a Telegram media"
        )
    start = datetime.now()
    file_name = input_str
    reply_message = await event.get_reply_message()
    c_time = time.time()
    downloaded_file_name = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, file_name)
    downloaded_file_name = await event.client.download_media(
        reply_message,
        downloaded_file_name,
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, batevent, c_time, "trying to download", file_name)
        ),
    )
    end = datetime.now()
    ms_one = (end - start).seconds

    # لتحويل الملف إلى mp3
    audio = AudioSegment.from_file(downloaded_file_name)
    
    # استخدام مكتبة tinytag للحصول على المعلومات الصوتية
    tag = TinyTag.get(downloaded_file_name)
    song_title = tag.title
    artist_name = tag.artist

    # إزالة الامتداد m4a من اسم الملف
    downloaded_file_name = os.path.splitext(downloaded_file_name)[0] + ".mp3"

    # إعادة تسمية الملف
    if artist_name and song_title:
        downloaded_file_name = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, f"{artist_name} - {song_title}.mp3")

    audio.export(downloaded_file_name, format="mp3", tags={'title': song_title, 'artist': artist_name})

    try:
        thumb = await reply_message.download_media(thumb=-1)
    except Exception:
        thumb = thumb
    if not os.path.exists(downloaded_file_name):
        return await batevent.edit(f"File Not Found {input_str}")
    c_time = time.time()
    caat = await event.client.send_file(
        event.chat_id,
        downloaded_file_name,
        force_document=forcedoc,
        supports_streaming=supsstream,
        allow_cache=False,
        reply_to=reply_to_id,
        thumb=thumb,
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, event, c_time, "trying to upload", downloaded_file_name)
        ),
    )
    end_two = datetime.now()
    os.remove(downloaded_file_name)
    ms_two = (end_two - end).seconds
    await edit_delete(
        batevent,
        f"`تم تحميل الملف في {ms_one} ثواني.\nAnd رفعة {ms_two} ثواني.`",
    )