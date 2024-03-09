#luc_md9
import contextlib
import os
import subprocess

from ..Config import Config
from ..helpers.tools import media_type
from . import lucmd9, edit_or_reply

plugin_category = "tools"

# تحديث دالة media_type
async def media_type(msg):
    try:
        if msg.media:
            return msg.media.document.mime_type.split("/")[0]
        elif msg.text:
            return "text"
        else:
            return "unknown"
    except Exception:
        return "unknown"

@lucmd9.ar_cmd(
    pattern="جيبها(?:\s|$)([\s\S]*)",
    command=("جيبها", plugin_category),
    info={
        "header": "لتحميل الوسائط من القناة",
        "description": "قم بتغيير اسم المستخدم وعدد الرسائل الأخيرة للتحقق من الأمر \
              لذلك سيقوم اليوزربوت بتنزيل ملفات الوسائط من آخر عدد من الرسائل إلى الخادم ",
        "usage": "{tr}جيبها count channel_username",
        "examples": "{tr}جيبها 10 @يوزر القناة",
    },
)
async def get_media(event):
    try:
        BAT = event.pattern_match.group(1)
        if not BAT:
            return await event.edit("`يرجى تحديد عدد الرسائل واسم المستخدم للقناة`")

        limit, channel_username = map(str, BAT.split(" ", 1))
        limit = int(limit)

        tempdir = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, channel_username)
        with contextlib.suppress(FileExistsError):
            os.makedirs(tempdir)

        event = await edit_or_reply(event, "`يتم التحميل من هذه القناة.....`")
        msgs = await event.client.get_messages(channel_username, limit=limit)

        i = 0
        for msg in msgs:
            mediatype = await media_type(msg)
            if mediatype != "unknown":
                await event.client.download_media(msg, tempdir)
                i += 1
                await event.edit(f"Downloading Media From this Channel.\n **DOWNLOADED : **`{i}`")

        files_count = len(os.listdir(tempdir))
        await event.edit(f"Successfully downloaded {files_count} number of media files from {channel_username} to tempdir")

    except Exception as e:
        await event.edit(f"Error: {str(e)}")

@lucmd9.ar_cmd(
    pattern="جيبها كلها(?:\s|$)([\s\S]*)",
    command=("جيبها كلها", plugin_category),
    info={
        "header": "لتحميل كلشي بالقناة ",
        "description": "قم بتغير اسم المستخدم وعدد الرسائل الأخيرة للتحقق من الأمر \
              لذلك سيقوم السورس بتنزيل ملفات الوسائط من آخر عدد من الرسائل إلى الخادم ",
        "note": "حبي السورس حده يحفط 3000 رسالة مو تبعص",
        "usage": "{tr}جيبها كلها channel_username",
        "examples": "{tr}جيبها كلها @اسم القناة",
    },
)
async def get_media(event):
    channel_username = event.pattern_match.group(1)
    tempdir = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, channel_username)
    with contextlib.suppress(BaseException):
        os.makedirs(tempdir)
    event = await edit_or_reply(event, "`يتم التحميل كل المحتوى .`")
    msgs = await event.client.get_messages(channel_username, limit=3000)
    i = 0
    for msg in msgs:
        mediatype = await media_type(msg)
        if mediatype is not None:
            await event.client.download_media(msg, tempdir)
            i += 1
            await event.edit(
                f"Downloading Media From this Channel.\n **DOWNLOADED : **`{i}`"
            )
    ps = subprocess.Popen(("ls", tempdir), stdout=subprocess.PIPE)
    output = subprocess.check_output(("wc", "-l"), stdin=ps.stdout)
    ps.wait()
    output = str(output)
    output = output.replace("b'", "")
    output = output.replace("\\n'", "")
    await event.edit(
        f"تم التحميل بنجاح {output} لعدد الفايل من {channel_username} "
    )
#🦇🦇🦇🦇🦇