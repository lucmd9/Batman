from telethon import events
import asyncio
import random
from telethon.tl.types import MessageEntityMentionName
from collections import deque

from ..helpers.utils import edit_or_reply
from . import lucmd9, ALIVE_NAME, plugin_category

plugin_category = "fun"
progs = [1045489068]

all_emojis = ["😎", "🚀", "🎉", "😄", "👍", "❤️", "🌟", "🤔", "😂", "🔥"]

@lucmd9.ar_cmd(
    pattern="سباق$",
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
            events.NewMessage(
                from_users=event.chat_id,
                incoming=True,
                func=lambda e: not e.via_bot_id
            ),
            timeout=30
        )

        if response.text and response.text.lower().strip() == correct_emoji:
            await edit_or_reply(event, f"تهانينا! {response.sender_id} فاز في السباق!")
        else:
            await edit_or_reply(event, "بعد وكت عوف السباق احسن.")
    except asyncio.TimeoutError:
        await edit_or_reply(event, "ولا واحد بي خير يدز ايموجي الصح.")  # تم تصحيح هنا

# ...