#امر تاخذ سكرين للمواقع
#————————BATT—————————-#LUC_MD9


import io
from datetime import datetime
import requests
from validators.url import url
from BATT import lucmd9
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.google_tools import chromeDriver
from ..helpers.utils import reply_id

plugin_category = "utils"


@lucmd9.ar_cmd(
    pattern="(سكرنلي|سكرن)(?:\s|$)([\s\S]*)",
    command=("سكرن", plugin_category),
)
async def _(event):
    cmd = event.pattern_match.group(1)
    text = event.pattern_match.group(2)
    reply = await event.get_reply_message()
    reply_to_id = await reply_id(event)
    if not text and reply:
        text = reply.text
    if not text:
        return await edit_delete(event, "اصبر بعد اخوك ...")
    if cmd == "s;vk":
        caturl = url(text)
        if not caturl:
            text = f"http://{text}"
            caturl = url(text)
        if not caturl:
            return await edit_delete(event, "همممم هذا الرابط غير مدعوم")
    elif cmd == "سكرنلي":
        text = f"https://www.google.com/search?q={text}"
    batevent = await edit_or_reply(event, "يتم التحميل ...")
    image, response = await chromeDriver.get_screenshot(text, batevent)
    if not image:
        return await edit_delete(batevent, response)

    await batevent.delete()
    with io.BytesIO(image) as out_file:
        out_file.name = f"{text}.PNG"
        await event.client.send_file(
            event.chat_id,
            out_file,
            caption=response,
            force_document=True,
            reply_to=reply_to_id,
            allow_cache=False,
            silent=True,
        )
        
      #جميع حقوق لسورس الخفاش تبوكه انيجك
