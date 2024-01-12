import json
import os
import re

from telethon.events import CallbackQuery

from BATT import lucmd9


@lucmd9.tgbot.on(CallbackQuery(data=re.compile(b"rzan_(.*)")))
async def on_plug_in_callback_query_handler(event):
    timestamp = int(event.pattern_match.group(1).decode("UTF-8"))
    if os.path.exists("./BATT/secrets.txt"):
        jsondata = json.load(open("./BATT/secrets.txt"))
        try:
            message = jsondata[f"{timestamp}"]
            userid = message["userid"]
            ids = [userid, lucmd9.uid]
            if event.query.user_id in ids:
                encrypted_tcxt = message["text"]
                reply_pop_up_alert = encrypted_tcxt
            else:
                reply_pop_up_alert = "⌯︙عـذرا هذه الهـمسة ليست مخصصة لـك"
        except KeyError:
            reply_pop_up_alert = "⌯︙عـذرا هذه الهمسة لم تعد موجوده في سيـرفرات الخفاش"
    else:
        reply_pop_up_alert = "⌯︙عـذرا هذه الهمسة لم تعد موجوده  "
    await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
