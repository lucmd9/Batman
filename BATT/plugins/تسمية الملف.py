#luc_md9
import asyncio
import os
import time
from datetime import datetime
import eyed3  # تم استيراد مكتبة eyed3

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
    
    # جزء جديد يقوم بالتحقق مما إذا كان الملف هو MP3
    file_name = input_str
    reply_message = await event.get_reply_message()
    if reply_message and reply_message.media and reply_message.media.document:
        if reply_message.media.document.mime_type == "audio/mpeg":
            audio_title = get_song_title(reply_message.file.name)
            if audio_title:
                file_name = f"{audio_title}.mp3"
    
    start = datetime.now()
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

# دالة جديدة للحصول على اسم الأغنية باستخدام مكتبة eyed3
def get_song_title(file_path):
    audio = eyed3.load(file_path)
    if audio.tag:
        return audio.tag.title
    return None
