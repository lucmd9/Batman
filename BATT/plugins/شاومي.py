from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from BATT import lucmd9
from BATT.core.managers import edit_or_reply

plugin_category = "extra"


@lucmd9.cat_cmd(
    pattern="شاومي ([\s\S]*)",
    command=("شاومي", plugin_category),
    info={
        "header": "To get lastest Firmware.",
        "description": "فقط في اجهزة الشاومي يعمل هذا الامر",
        "استعمل": "{tr}شاومي <اسم كود للجهاز>",
        "مثال": "{tr}شاومي whyred",
    },
)
async def _(event):
    "اخر معلومات."
    link = event.pattern_match.group(1)
    firmware = "شاومي"
    catevent = await edit_or_reply(event, "```اصبر```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{firmware} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await catevent.edit("```شيل البلوك من @XiaomiGeeksBot plox```")
        else:
            await catevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@lucmd9.ar_cmd(
    pattern="البائع ([\s\S]*)",
    command=("البائع", plugin_category),
    info={
        "header": "لجلب اخر بائع.",
        "description": "Works for Xiaomeme devices only",
        "استعمال": "{tr}البائع <اسم الكود>",
        "مثال": "{tr}البائع whyred",
    },
)
async def _(event):
    "لجلب اخر بائع."
    link = event.pattern_match.group(1)
    vendor = "البائع"
    catevent = await edit_or_reply(event, "```ثواني```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{vendor} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await catevent.edit("```Unblock @XiaomiGeeksBot plox```")
        else:
            await catevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@lucmd9.ar_cmd(
    pattern="معلومات شاومي ([\s\S]*)",
    command=("معلومات شاومي", plugin_category),
    info={
        "header": "To get quick spec information about device",
        "description": "Works for Xiaomeme devices only",
        "usage": "{tr}معلومات شاومي <اسم الكود>",
        "examples": "{tr}معلومات شاومي whyred",
    },
)
async def _(event):
    "To get quick spec information about device"
    link = event.pattern_match.group(1)
    specs = "specs"
    catevent = await edit_or_reply(event, "```دصبر```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{specs} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await catevent.edit("```Unblock @XiaomiGeeksBot plox```")
        else:
            await catevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@lucmd9.ar_cmd(
    pattern="fastboot ([\s\S]*)",
    command=("fastboot", plugin_category),
    info={
        "header": "To get latest fastboot MIUI.",
        "description": "Works for Xiaomeme devices only",
        "usage": "{tr}fastboot <codename>",
        "examples": "{tr}fastboot whyred",
    },
)
async def _(event):
    "To get latest fastboot MIUI."
    link = event.pattern_match.group(1)
    fboot = "fastboot"
    catevent = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{fboot} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await catevent.edit("```Unblock @XiaomiGeeksBot plox```")
        else:
            await catevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@lucmd9.ar_cmd(
    pattern="الاستعادة" ([\s\S]*)",
    command=("الاستعادة", plugin_category),
    info={
        "header": "To get latest recovery MIUI.",
        "description": "Works for Xiaomeme devices only",
        "usage": "{tr}recovery <codename>",
        "examples": "{tr}recovery whyred",
    },
)
async def _(event):
    "To get latest recovery MIUI."
    link = event.pattern_match.group(1)
    recovery = "recovery"
    catevent = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{recovery} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await catevent.edit("```Unblock @XiaomiGeeksBot plox```")
        else:
            await catevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@lucmd9.ar_cmd(
    pattern="pb ([\s\S]*)",
    command=("pb", plugin_category),
    info={
        "header": "To get latest PBRP.",
        "description": "Works for Xiaomeme devices only",
        "usage": "{tr}pb <codename>",
        "examples": "{tr}pb whyred",
    },
)
async def _(event):
    "To get latest PBRP."
    link = event.pattern_match.group(1)
    pitch = "pb"
    catevent = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{pitch} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await catevent.edit("```Unblock @XiaomiGeeksBot plox```")
        else:
            await catevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@lucmd9.ar_cmd(
    pattern="of ([\s\S]*)",
    command=("of", plugin_category),
    info={
        "header": "To get latest ORangeFox Recover.",
        "description": "Works for Xiaomeme devices only",
        "usage": "{tr}of <codename>",
        "examples": "{tr}of whyred",
    },
)
async def _(event):
    "To get latest ORangeFox Recover."
    link = event.pattern_match.group(1)
    ofox = "of"
    catevent = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{ofox} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await catevent.edit("```Unblock @XiaomiGeeksBot plox```")
        else:
            await catevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)