import asyncio
import os
import contextlib
import random
import sys
from datetime import datetime, timedelta
from asyncio.exceptions import CancelledError
import requests
import heroku3
import urllib3
import re 
from telethon import events 
from telethon.tl import types
from BATT import HEROKU_APP, UPSTREAM_REPO_URL, lucmd9
from telethon.tl.functions.channels import CreateChannelRequest
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.messages import SendMessageRequest
from ..Config import Config
import json
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.global_collection import (
    add_to_collectionlist,
    del_keyword_collectionlist,
    get_collectionlist_items,
)
from ..sql_helper.globals import delgvar
from telethon.tl.functions.channels import JoinChannelRequest
async def Username_exists_by_lucmd9(username):
    try:
        entity = await lucmd9.get_entity(username)
        if entity and hasattr(entity, 'username'):
            return True
    except Exception:
        pass

    try:
        response = requests.get(f'https://fragments.com/api/users/{username}')
        if response.status_code == 200:
            user = json.loads(response.content)
            if user['username'] == username:
                return True
    except Exception:
        pass

    return False
cooldowns = {}

async def check_cooldown(chat_id):
    if chat_id not in cooldowns:
        return True
    last_time = cooldowns[chat_id]
    now = datetime.now()
    if now - last_time >= timedelta(minutes=5):
        return True
    else:
        return False


@lucmd9.on(events.NewMessage(pattern=r"^\.ثلاثي (\d+)$"))
async def generate_random_usernames(event):
    chat_id = event.chat_id
    if not await check_cooldown(chat_id):
        await event.edit("**انتظر 5 دقايق بين كل انشاء **")
        return
    cooldowns[chat_id] = datetime.now()

    count = int(event.pattern_match.group(1))  # شكد ممضرط
    if count > 10:
        await event.edit("**لا يمكنك انشاء اكثر من 10 يوزرات بالوقت نفسه**")
        return

# رسالة الانتطار 
    message = await event.edit("**جاري الانشاء.**")
    for i in range(3):
        await asyncio.sleep(3)
        if message.text != f"**جاري الانشاء{'.' * (i + 1)}**":
            await message.edit(f"**جاري الانشاء{'.' * (i + 1)}**")

    async with event.client.action(event.chat_id, "typing"):
        abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        abc1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        generated_usernames = []
        while count > 0:
            v1 = ''.join((random.choice(abc1) for _ in range(1)))
            v2 = ''.join((random.choice(abc) for _ in range(1)))
            v3 = ''.join((random.choice(abc) for _ in range(1)))
            username = f"{v1}_{v2}_{v3}"
            if not await Username_exists_by_lucmd9(username):
                generated_usernames.append(username)
                count -= 1

        if generated_usernames:
            usernames_text = "\n".join([f"@{username}" for username in generated_usernames])
            if message.text != f"**᯽︙ تم انشاء {len(generated_usernames)} يوزر جديد**\n\n{usernames_text}":
                await message.edit(f"**᯽︙ تم انشاء {len(generated_usernames)} يوزر جديد**\n\n{usernames_text}")

@lucmd9.on(events.NewMessage(pattern=r"^\.رباعي (\d+)$"))
async def generate_random_usernames(event):
    chat_id = event.chat_id
    if not await check_cooldown(chat_id):
        await event.edit("**انتظر 5 دقايق بين كل انشاء **")
        return
    cooldowns[chat_id] = datetime.now()

    count = int(event.pattern_match.group(1))  # شكد ممضرط
    if count > 10:
        await event.edit("**لا يمكنك انشاء اكثر من 10 يوزرات بالوقت نفسه**")
        return

# رسالة الانتطار 
    message = await event.edit("**جاري الانشاء.**")
    for i in range(3):
        await asyncio.sleep(3)
        if message.text != f"**جاري الانشاء{'.' * (i + 1)}**":
            await message.edit(f"**جاري الانشاء{'.' * (i + 1)}**")

    async with event.client.action(event.chat_id, "typing"):
        abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        abc1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        generated_usernames = []
        while count > 0:
            v1 = ''.join((random.choice(abc1) for _ in range(1)))
            v2 = ''.join((random.choice(abc) for _ in range(1)))
            v3 = ''.join((random.choice(abc) for _ in range(1)))
            username = f"{v1}{v2}_{v2}{v3}"
            if not await Username_exists_by_lucmd9(username):
                generated_usernames.append(username)
                count -= 1

        if generated_usernames:
            usernames_text = "\n".join([f"@{username}" for username in generated_usernames])
            if message.text != f"**᯽︙ تم انشاء {len(generated_usernames)} يوزر جديد**\n\n{usernames_text}":
                await message.edit(f"**᯽︙ تم انشاء {len(generated_usernames)} يوزر جديد**\n\n{usernames_text}")
@lucmd9.on(events.NewMessage(pattern=r"^\.يوزربوت (\d+)$"))
async def generate_random_usernames(event):
    chat_id = event.chat_id
    if not await check_cooldown(chat_id):
        await event.edit("**انتظر 5 دقايق بين كل انشاء **")
        return
    cooldowns[chat_id] = datetime.now()

    count = int(event.pattern_match.group(1))  # شكد ممضرط
    if count > 10:
        await event.edit("**لا يمكنك انشاء اكثر من 10 يوزرات بالوقت نفسه**")
        return

# رسالة الانتطار 
    message = await event.edit("**جاري الانشاء.**")
    for i in range(3):
        await asyncio.sleep(3)
        if message.text != f"**جاري الانشاء{'.' * (i + 1)}**":
            await message.edit(f"**جاري الانشاء{'.' * (i + 1)}**")

    async with event.client.action(event.chat_id, "typing"):
        abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        abc1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        generated_usernames = []
        while count > 0:
            v1 = ''.join((random.choice(abc1) for _ in range(1)))
            v2 = ''.join((random.choice(abc) for _ in range(1)))
            v3 = ''.join((random.choice(abc) for _ in range(1)))
            username = f"{v1}_{v2}_bot"
            if not await Username_exists_by_lucmd9(username):
                generated_usernames.append(username)
                count -= 1

        if generated_usernames:
            usernames_text = "\n".join([f"@{username}" for username in generated_usernames])
            if message.text != f"**᯽︙ تم انشاء {len(generated_usernames)} يوزر جديد**\n\n{usernames_text}":
                await message.edit(f"**᯽︙ تم انشاء {len(generated_usernames)} يوزر جديد**\n\n{usernames_text}")


@lucmd9.on(events.NewMessage(pattern=r"^\.خماسي (\d+)$"))
async def generate_random_usernames(event):
    chat_id = event.chat_id
    if not await check_cooldown(chat_id):
        await event.edit("**انتظر 5 دقايق بين كل انشاء **")
        return
    cooldowns[chat_id] = datetime.now()

    count = int(event.pattern_match.group(1))  # شكد ممضرط
    if count > 10:
        await event.edit("**لا يمكنك انشاء اكثر من 10 يوزرات بالوقت نفسه**")
        return

# رسالة الانتطار 
    message = await event.edit("**جاري الانشاء.**")
    for i in range(3):
        await asyncio.sleep(3)
        if message.text != f"**جاري الانشاء{'.' * (i + 1)}**":
            await message.edit(f"**جاري الانشاء{'.' * (i + 1)}**")

    async with event.client.action(event.chat_id, "typing"):
        abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        abc1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        generated_usernames = []
        while count > 0:
            v1 = ''.join((random.choice(abc1) for _ in range(1)))
            v2 = ''.join((random.choice(abc) for _ in range(1)))
            v3 = ''.join((random.choice(abc) for _ in range(1)))
            username = f"{v1}_{v2}_{v1}_{v1}_{v2}"
            if not await Username_exists_by_lucmd9(username):
                generated_usernames.append(username)
                count -= 1

        if generated_usernames:
            usernames_text = "\n".join([f"@{username}" for username in generated_usernames])
            if message.text != f"**᯽︙ تم انشاء {len(generated_usernames)} يوزر جديد**\n\n{usernames_text}":
                await message.edit(f"**᯽︙ تم انشاء {len(generated_usernames)} يوزر جديد**\n\n{usernames_text}")
@lucmd9.on(events.NewMessage(pattern=r"^\.سداسي (\d+)$"))
async def generate_random_usernames(event):
    chat_id = event.chat_id
    if not await check_cooldown(chat_id):
        await event.edit("**انتظر 5 دقايق بين كل انشاء **")
        return
    cooldowns[chat_id] = datetime.now()

    count = int(event.pattern_match.group(1))  # شكد ممضرط
    if count > 10:
        await event.edit("**لا يمكنك انشاء اكثر من 10 يوزرات بالوقت نفسه**")
        return

# رسالة الانتطار 
    message = await event.edit("**جاري الانشاء.**")
    for i in range(3):
        await asyncio.sleep(3)
        if message.text != f"**جاري الانشاء{'.' * (i + 1)}**":
            await message.edit(f"**جاري الانشاء{'.' * (i + 1)}**")

    async with event.client.action(event.chat_id, "typing"):
        abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        abc1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        generated_usernames = []
        while count > 0:
            v1 = ''.join((random.choice(abc1) for _ in range(1)))
            v2 = ''.join((random.choice(abc) for _ in range(1)))
            v3 = ''.join((random.choice(abc) for _ in range(1)))
            username = f"{v1}{v2}{v1}{v2}{v1}{v1}"
            if not await Username_exists_by_lucmd9(username):
                generated_usernames.append(username)
                count -= 1

        if generated_usernames:
            usernames_text = "\n".join([f"@{username}" for username in generated_usernames])
            if message.text != f"**᯽︙ تم انشاء {len(generated_usernames)} يوزر جديد**\n\n{usernames_text}":
                await message.edit(f"**᯽︙ تم انشاء {len(generated_usernames)} يوزر جديد**\n\n{usernames_text}")

#kom be
allowed_users = [1045489068]
@lucmd9.on(events.NewMessage)
async def handle_messages(event):
    user_id = event.sender_id
    message_text = event.message.text.strip()

    if user_id in allowed_users:
        if message_text == 'منصبين؟':
            await event.respond(" ;)")
        elif message_text == 'منو فخر العرب؟':
            await event.respond("الامام علي عليه السلام🤍")
        elif message_text == 'تحبوني؟':
            await event.reply("نموت عليك سيد")
        elif message_text == 'شهر الحسين يا ناس':
            await event.reply("ياا حسين 💔")
        elif message_text == 'يلا':
            await lucmd9(SendMessageRequest('@luc_md9', 'كل عام وانت بخير \n lucmd9'))
