import time

from prettytable import PrettyTable

from BATT import lucmd9

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.tools import media_type
from ..helpers.utils import _format
from . import humanbytes

plugin_category = "utils"


TYPES = [
    "Photo",
    "Audio",
    "Video",
    "Document",
    "Sticker",
    "Gif",
    "Voice",
    "Round Video",
]



def weird_division(n, d):
    return n / d if d else 0


@lucmd9.ar_cmd(
    pattern="تخزين الكروب(?:\s|$)([\s\S]*)",
    command=("تخزين الكروب", plugin_category),
    info={
        "header": "Shows you the complete media/file summary of the that group.",
        "description": "As of now limited to last 10000 in the group u used",
        "usage": "{tr}تخزين الكروب <المعرف/الايدي>",
        "examples": "{tr}تخزين الكروب @catuserbot_support",
    },
)
async def _(event):  # sourcery no-metrics
    "Shows you the complete media/file summary of the that group"
    entity = event.chat_id
    input_str = event.pattern_match.group(1)
    if input_str:
        try:
            entity = int(input_str)
        except ValueError:
            entity = input_str
    starttime = int(time.monotonic())
    x = PrettyTable()
    totalcount = totalsize = msg_count = 0
    x.title = "مـلخص الـمستخدم"
    x.field_names = ["Media", "Count", "File size"]
    largest = "   <b>اكـبـر حـجـم</b>\n"
    try:
        chatdata = await event.client.get_entity(entity)
    except Exception as e:
        return await edit_delete(
            event, f"<b>᯽︙ خـطـأ : </b><code>{str(e)}</code>", time=5, parse_mode="HTML"
        )
    if type(chatdata).__name__ == "Channel":
        if chatdata.username:
            link = f"<a href='t.me/{chatdata.username}'>{chatdata.title}</a>"
        else:
            link = chatdata.title
    else:
        link = f"<a href='tg://user?id={chatdata.id}'>{chatdata.first_name}</a>"
    catevent = await edit_or_reply(
        event,
        f"<code>عـدد الملفات وحـجم الـملف من </code><b>{link}</b>\n<code>قـد تـأخذ بـعض الـوقت انهـا تعتـمد عـلى عـدد الرسـائـل</code>",
        parse_mode="HTML",
    )
    media_dict = {
        m: {"file_size": 0, "count": 0, "max_size": 0, "max_file_link": ""}
        for m in TYPES
    }
    async for message in event.client.iter_messages(entity=entity, limit=None):
        msg_count += 1
        media = media_type(message)
        if media is not None:
            media_dict[media]["file_size"] += message.file.size
            media_dict[media]["count"] += 1
            if message.file.size > media_dict[media]["max_size"]:
                media_dict[media]["max_size"] = message.file.size
                if type(chatdata).__name__ == "Channel":
                    media_dict[media][
                        "max_file_link"
                    ] = f"https://t.me/c/{chatdata.id}/{message.id}"  # pylint: disable=line-too-long
                else:
                    media_dict[media][
                        "max_file_link"
                    ] = f"tg://openmessage?user_id={chatdata.id}&message_id={message.id}"  # pylint: disable=line-too-long
            totalsize += message.file.size
            totalcount += 1
    for mediax in TYPES:
        x.add_row(
            [
                mediax,
                media_dict[mediax]["count"],
                humanbytes(media_dict[mediax]["file_size"]),
            ]
        )
        if media_dict[mediax]["count"] != 0:
            largest += f"  •  <b><a href='{media_dict[mediax]['max_file_link']}'>{mediax}</a>  : </b><code>{humanbytes(media_dict[mediax]['max_size'])}</code>\n"
    endtime = int(time.monotonic())
    if endtime - starttime >= 120:
        runtime = str(round(((endtime - starttime) / 60), 2)) + " من الـدقائق"
    else:
        runtime = str(endtime - starttime) + " مـن الـثواني"
    avghubytes = humanbytes(weird_division(totalsize, totalcount))
    avgruntime = (
        str(round((weird_division((endtime - starttime), totalcount)) * 1000, 2))
        + " ms"
    )
    totalstring = f"<code><b>᯽︙ جمـيع الـملفات 🕷 </b>       | {str(totalcount)}\
                  \n᯽︙ حجـم الـملف الكـلي 🕷    | {humanbytes(totalsize)}\
                  \n᯽︙ حـجم الـملف 🕷    | {avghubytes}\
                  \n</code>"
    runtimestring = f"<code>᯽︙ وقـت الـتشغيل 🕷            | {runtime}\
                    \n᯽︙ وقـت الـتشغيل لـكل مـلف 🕷    | {avgruntime}\
                    \n</code>"
    line = "<code>+--------------------+-----------+</code>\n"
    result = f"<b>᯽︙ الـكـروب : {link}</b>\n\n"
    result += f"<code>᯽︙ جـميـع الـرسائـل: {msg_count}</code>\n"
    result += "<b>᯽︙ مـلخص الـملف : </b>\n"
    result += f"<code>{str(x)}</code>\n"
    result += f"{largest}"
    result += line + totalstring + line + runtimestring + line
    await catevent.edit(result, parse_mode="HTML", link_preview=False)


@lucmd9.ar_cmd(
    pattern="تخزين المستخدم(?:\s|$)([\s\S]*)",
    command=("تخزين المستخدم", plugin_category),
    info={
        "header": "Shows you the complete media/file summary of the that user in that group.",
        "description": "As of now limited to last 10000 messages of that person in the group u used",
        "usage": "{tr}userfs <reply/username/id>",
        "examples": "{tr}userfs @MissRose_bot",
    },
)
async def _(event):  # sourcery no-metrics
    "Shows you the complete media/file summary of the that user in that group."
    reply = await event.get_reply_message()
    input_str = event.pattern_match.group(1)
    if reply and input_str:
        try:
            entity = int(input_str)
        except ValueError:
            entity = input_str
        userentity = reply.sender_id
    elif reply:
        entity = event.chat_id
        userentity = reply.sender_id
    elif input_str:
        entity = event.chat_id
        try:
            userentity = int(input_str)
        except ValueError:
            userentity = input_str
    else:
        entity = event.chat_id
        userentity = event.sender_id
    starttime = int(time.monotonic())
    x = PrettyTable()
    totalcount = totalsize = msg_count = 0
    x.title = "مـلخص الـمستخدم"
    x.field_names = ["Media", "Count", "File size"]
    largest = "   <b>اكبـر حـجـم</b>\n"
    try:
        chatdata = await event.client.get_entity(entity)
    except Exception as e:
        return await edit_delete(
            event, f"<b>خـطأ : </b><code>{str(e)}</code>", 5, parse_mode="HTML"
        )
    try:
        userdata = await event.client.get_entity(userentity)
    except Exception as e:
        return await edit_delete(
            event, f"<b>خـطأ : </b><code>{str(e)}</code>", time=5, parse_mode="HTML"
        )
    if type(chatdata).__name__ == "Channel":
        if chatdata.username:
            link = f"<a href='t.me/{chatdata.username}'>{chatdata.title}</a>"
        else:
            link = chatdata.title
    else:
        link = f"<a href='tg://user?id={chatdata.id}'>{chatdata.first_name}</a>"
    catevent = await edit_or_reply(
        event,
        f"<code>عدد الملفات وحجم الملف من </code>{_format.htmlmentionuser(userdata.first_name,userdata.id)}<code> فـي الـكروب </code><b>{link}</b>\n<code>ربـما تأخـذ بعـض الوقـت تعـتمد عـلى عـدد رسـائل المـستـخدم</code>",
        parse_mode="HTML",
    )

    media_dict = {
        m: {"file_size": 0, "count": 0, "max_size": 0, "max_file_link": ""}
        for m in TYPES
    }
    async for message in event.client.iter_messages(
        entity=entity, limit=None, from_user=userentity
    ):
        msg_count += 1
        media = media_type(message)
        if media is not None:
            media_dict[media]["file_size"] += message.file.size
            media_dict[media]["count"] += 1
            if message.file.size > media_dict[media]["max_size"]:
                media_dict[media]["max_size"] = message.file.size
                if type(chatdata).__name__ == "Channel":
                    media_dict[media][
                        "max_file_link"
                    ] = f"https://t.me/c/{chatdata.id}/{message.id}"
                else:
                    media_dict[media][
                        "max_file_link"
                    ] = f"tg://openmessage?user_id={chatdata.id}&message_id={message.id}"
            totalsize += message.file.size
            totalcount += 1
    for mediax in TYPES:
        x.add_row(
            [
                mediax,
                media_dict[mediax]["count"],
                humanbytes(media_dict[mediax]["file_size"]),
            ]
        )
        if media_dict[mediax]["count"] != 0:
            largest += f"  •  <b><a href='{media_dict[mediax]['max_file_link']}'>{mediax}</a>  : </b><code>{humanbytes(media_dict[mediax]['max_size'])}</code>\n"
    endtime = int(time.monotonic())
    if endtime - starttime >= 120:
        runtime = str(round(((endtime - starttime) / 60), 2)) + " من الدقائق"
    else:
        runtime = str(endtime - starttime) + " من الثوانـي"
    avghubytes = humanbytes(weird_division(totalsize, totalcount))
    avgruntime = (
        str(round((weird_division((endtime - starttime), totalcount)) * 1000, 2))
        + " ms"
    )
    totalstring = f"<code> ᯽︙ إجمالـي الملفـات 🕷 :    | {str(totalcount)}\
                  \n ᯽︙ الحجـم الإجمالـي للملـف 🕷 :   | {humanbytes(totalsize)}\
                  \n ᯽︙ حجم الملف  :  | {avghubytes}\
                  \n</code>"
    runtimestring = f"<code> ᯽︙ وقـت التشغيـل 🕷 :            | {runtime}\
                    \n وقـت التشغيـل لـكـل ملـف 🕷 : | {avgruntime}\
                    \n</code>"
    line = "<code>+--------------------+-----------+</code>\n"
    result = f"᯽︙ المجموعـة 🕷 : {link}\nUser : {_format.htmlmentionuser(userdata.first_name,userdata.id)}\n\n"
    result += f"<code>᯽︙ مجمـوع الرسائـل 🕷 : {msg_count}</code>\n"
    result += "⌔︙ملخـص الملـف 🕷 :\n"
    result += f"<code>{str(x)}</code>\n"
    result += f"{largest}"
    result += line + totalstring + line + runtimestring + line
    await catevent.edit(result, parse_mode="HTML", link_preview=False)
