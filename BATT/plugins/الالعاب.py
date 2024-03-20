from BATT import lucmd9
from ..core.managers import edit_or_reply
from datetime import datetime
import random
from telethon import events
import emoji
import asyncio

plugin_category = "fun"

all_emojis = emoji.UNICODE_EMOJI.keys()

@lucmd9.on(events.NewMessage(pattern='.ايموج'))
async def emoji_race(event):
    race_emoji = random.choice(list(all_emojis))
    start_time = datetime.now()
    await edit_or_reply(event, f"اول واحد يرسل هذا الإيموجي {race_emoji} يفوز!")

    async with lucmd9.conversation(event.chat_id) as conv:
        while True:
            response = await conv.wait_event(events.NewMessage(incoming=True, from_users=event.chat_id))
            if race_emoji in response.message:
                break

    end_time = datetime.now()
    time_taken = (end_time - start_time).total_seconds()
    winner = await lucmd9.get_entity(response.sender_id)
    await response.reply(f"🎉 علكيفك سونيك فزت[{winner.first_name}](tg://user?id={winner.id}) \n- الثواني: {int(time_taken)} !!", parse_mode="md")