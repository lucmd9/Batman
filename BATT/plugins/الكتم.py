import base64
import asyncio
from datetime import datetime

from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChatBannedRights
from telethon.utils import get_display_name
from telethon.tl.types import ChannelParticipantsAdmins

from BATT import lucmd9

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _format
from ..sql_helper import gban_sql_helper as gban_sql
from ..sql_helper.mute_sql import is_muted, mute, unmute
from . import BOTLOG, BOTLOG_CHATID, admin_groups, get_user_from_event

plugin_category = "admin"


joker_mute = "https://telegra.ph/file/0043454e2417ac7ca0e94.jpg"
joker_unmute = "https://telegra.ph/file/0fb9c22b069918db0dea1.jpg"
#=================== الكـــــــــــــــتم  ===================  #

@lucmd9.ar_cmd(pattern=f"كتم(?:\s|$)([\s\S]*)")
async def mutejep(event):
    await event.delete()
    if event.is_private:
        replied_user = await event.client.get_entity(event.chat_id)
        if is_muted(event.chat_id, event.chat_id):
            return await event.edit(
                "**- هـذا المسـتخـدم مڪتـوم . . سـابقـاً **"
            )
        if event.chat_id == lucmd9.uid:
            return await edit_or_reply(event, "**𖡛... . لمـاذا تࢪيـد كتم نفسـك؟  ...𖡛**")
        if event.chat_id == 6205161271:
            return await edit_or_reply(event, "** دي . . لا يمڪنني كتـم مطـور السـورس  ╰**")
        if event.chat_id == 1045489068:
            return await edit_or_reply(event, "** دي . . لا يمڪنني كتـم مطـور السـورس  ╰**")
        if event.chat_id == 5762222122:
            return await edit_or_reply(event, "** دي . . لا يمڪنني كتـم مطـور السـورس  ╰**")
        if event.chat_id == 6295913543:
            return await edit_or_reply(event, "** دي . . لا يمڪنني كتـم مطـور السـورس  ╰**")                
        try:
            mute(event.chat_id, event.chat_id)
        except Exception as e:
            await event.edit(f"**- خطـأ **\n`{e}`")
        else:
            return await event.client.send_file(
                event.chat_id,
                joker_mute,
                caption="** تم ڪتـم الـمستخـدم  . . بنجـاح 🔕✓**",
            )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#كتــم_الخــاص\n"
                f"**- الشخـص  :** [{replied_user.first_name}](tg://user?id={event.chat_id})\n",
            )
    else:
        chat = await event.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            return await edit_or_reply(
                event, "** أنـا لسـت مشـرف هنـا ؟!! .**"
            )
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == lucmd9.uid:
            return await edit_or_reply(event, "**𖡛... . لمـاذا تࢪيـد كتم نفسـك؟  ...𖡛**")
        if user.id == 6205161271:
            return await edit_or_reply(event, "** دي . . لا يمڪنني كتـم مطـور السـورس  ╰**")
        if user.id == 1045489068:
            return await edit_or_reply(event, "** دي . . لا يمڪنني كتـم مطـور السـورس  ╰**")
        if user.id == 5762222122:
            return await edit_or_reply(event, "** دي . . لا يمڪنني كتـم مطـور السـورس  ╰**")
        if is_muted(user.id, event.chat_id):
            return await edit_or_reply(
                event, "**عــذراً .. هـذا الشخـص مكتــوم سـابقــاً هنـا**"
            )
        result = await event.client.get_permissions(event.chat_id, user.id)
        try:
            if result.participant.banned_rights.send_messages:
                return await edit_or_reply(
                    event,
                    "**عــذراً .. هـذا الشخـص مكتــوم سـابقــاً هنـا**",
                )
        except AttributeError:
            pass
        except Exception as e:
            return await edit_or_reply(event, f"**- خطــأ : **`{e}`")
        try:
            mute(user.id, event.chat_id)
        except UserAdminInvalidError:
            if "admin_rights" in vars(chat) and vars(chat)["admin_rights"] is not None:
                if chat.admin_rights.delete_messages is not True:
                    return await edit_or_reply(
                        event,
                        "**- عــذراً .. ليـس لديـك صـلاحيـة حـذف الرسـائل هنـا**",
                    )
            elif "creator" not in vars(chat):
                return await edit_or_reply(
                    event, "**- عــذراً .. ليـس لديـك صـلاحيـة حـذف الرسـائل هنـا**"
                )
        except Exception as e:
            return await edit_or_reply(event, f"**- خطــأ : **`{e}`")
        if reason:
            await event.client.send_file(
                event.chat_id,
                joker_mute,
                caption=f"**- المستخـدم :** {_format.mentionuser(user.first_name ,user.id)}  \n**- تـم كتمـه بنجـاح ✓**\n\n**- السـبب :** {reason}",
            )
        else:
            await event.client.send_file(
                event.chat_id,
                joker_mute,
                caption=f"**- المستخـدم :** {_format.mentionuser(user.first_name ,user.id)}  \n**- تـم كتمـه بنجـاح ✓**\n\n",
            )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#الكــتم\n"
                f"**الشخـص :** [{user.first_name}](tg://user?id={user.id})\n"
                f"**الدردشـه :** {get_display_name(await event.get_chat())}(`{event.chat_id}`)",
            ) 
#=================== الغـــــــــــــاء الكـــــــــــــــتم  ===================  #

@lucmd9.ar_cmd(pattern=f"(الغاء الكتم|الغاء كتم)(?:\s|$)([\s\S]*)")
async def unmutejep(event):
    await event.delete()
    if event.is_private:
        replied_user = await event.client.get_entity(event.chat_id)
        if not is_muted(event.chat_id, event.chat_id):
            return await event.edit(
                "**عــذراً .. هـذا الشخـص غيــر مكتــوم هنـا**"
            )
        try:
            unmute(event.chat_id, event.chat_id)
        except Exception as e:
            await event.edit(f"**- خطــأ **\n`{e}`")
        else:
            await event.client.send_file(
                event.chat_id,
                joker_unmute,
                caption="**- تـم الغــاء كتــم الشخـص هنـا .. بنجــاح ✓**",
            )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#الغــاء_الكــتم\n"
                f"**- الشخـص :** [{replied_user.first_name}](tg://user?id={event.chat_id})\n",
            )
    else:
        user, _ = await get_user_from_event(event)
        if not user:
            return
        try:
            if is_muted(user.id, event.chat_id):
                unmute(user.id, event.chat_id)
            else:
                result = await event.client.get_permissions(event.chat_id, user.id)
                if result.participant.banned_rights.send_messages:
                    await event.client(
                        EditBannedRequest(event.chat_id, user.id, UNBAN_RIGHTS)
                    )
        except AttributeError:
            return await edit_or_reply(
                event,
                "**- الشخـص غيـر مكـتـوم**",
            )
        except Exception as e:
            return await edit_or_reply(event, f"**- خطــأ : **`{e}`")
        await event.client.send_file(
            event.chat_id,
            joker_unmute,
            caption=f"**- المستخـدم :** {_format.mentionuser(user.first_name ,user.id)} \n**- تـم الغـاء كتمـه بنجـاح ✓**",
        )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#الغــاء_الكــتم\n"
                f"**- الشخـص :** [{user.first_name}](tg://user?id={user.id})\n"
                f"**- الدردشــه :** {get_display_name(await event.get_chat())}(`{event.chat_id}`)",
            )



@lucmd9.ar_cmd(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "كتم_مؤقت"):
        await event.delete
# ===================================== # 
