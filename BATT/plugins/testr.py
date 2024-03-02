from collections import deque
from telethon import events
import asyncio#
from telethon import events
import random
from ..helpers.utils import _format
from . import ALIVE_NAME, lucmd9, edit_or_reply
trom config import config
#امر أسرع ايموجي فقط في سورس الخفاش 

# ...

all_emojis = ["😎", "🚀", "🎉", "😄", "👍", "❤️", "🌟", "🤔", "😂", "🔥"]

@lucmd9.ar_cmd(
    pattern="أسرع سباق$",
    command=("سباق", plugin_category),
    info={
        "الامر": "سباق لإرسال أسرع إيموجي",
        "الاستخدام": "{tr}سباق",
    },
)
async def emoji_race(event):
    "emoji race command"
    correct_emoji = random.choice(all_emojis)

    message = f"أسرع إيموجي: {correct_emoji}"
    await edit_or_reply(event, message)

    try:
        response = await event.client.wait_for(
            events.NewMessage(func=lambda e: e.sender_id != event.client.uid),
            timeout=30
        )

        if response.text and response.text.lower().strip() == correct_emoji:
            await event.reply(f"تهانينا! {response.sender_id} فاز في السباق!")
        else:
            await event.reply("بعد وكت عوف السباق احسن.")
    except asyncio.TimeoutError:
        await event.reply("ولا واحد بي خير يدز ايموجي الصح.")

#فقط في سورس الخفاش 🦇