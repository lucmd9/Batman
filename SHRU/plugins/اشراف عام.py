#    جميع الحقوق محفوظة كتابة وتعديل  :   @SX9OO
#    اخمط مع ذكر الحقوق غيرها انت مطور فاشل
marculs=9
from telethon.errors.rpcerrorlist import (UserIdInvalidError,
                                            MessageTooLongError)
from telethon.tl.functions.channels import (EditAdminRequest,
                                              EditBannedRequest,
                                                EditPhotoRequest)
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.types import (ChannelParticipantsAdmins,
                                 ChatAdminRights,
                                   ChatBannedRights,
                                     MessageEntityMentionName,
                                       MessageMediaPhoto)
from batt.utils import admin_cmd
from ..Config import Config
from batt import CMD_HELP, lucmd9
up_admin = Config.UP_ET or "ارفع"
down_admin = Config.DOWN_ET or "تزل"
async def get_full_user(event):  
    args = event.pattern_match.group(1).split(':', 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("▾∮ لا يمكنك بدون ايدي المستخدم")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await event.edit("▾∮ هنالك خطأ يرجى تبليغنا @angthon", str(err))           
    return user_obj, extra

global hawk,moth
hawk="admin"
moth="owner"
async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj
@lucmd9.on(admin_cmd(pattern="{up_admin} ?(.*)"))
async def gben(batt):
    dc = razan = batt
    i = 0
    sender = await dc.get_sender()
    me = await batt.client.get_me()
    await razan.edit("▾∮ يتم رفع المستخدم في جميع المجموعات")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await batt.get_chat()
    if batt.is_private:
        user = batt.chat
        rank = batt.pattern_match.group(1)
    else:
        batt.chat.title
    try:
        user, rank = await get_full_user(batt)
    except:
        pass
    if me == user:
       lucmd9 = await razan.edit("▾∮ لا استطيع رفع نفسي ،")
       return
    try:
        if not rank:
            rank = "ㅤㅤ"
    except:
        return await razan.edit(f"**▾∮ هنالك شي خطأ**")
    if user:
        telchanel = [d.entity.id
                     for d in await batt.client.get_dialogs()
                     if (d.is_group or d.is_channel)
                     ]
        rgt = ChatAdminRights(add_admins=True,
                               invite_users=True,
                                change_info=True,
                                 ban_users=True,
                                  delete_messages=True,
                                   pin_messages=True)
        for x in telchanel:
          try:
             await batt.client(EditAdminRequest(x, user, rgt, rank))
             i += 1
             await razan.edit(f"**▾∮ يتم الرفع في **: `{i}` من المجموعات")
          except:
             pass
    else:
        await razan.edit(f"**▾∮ يجب عليك الرد على المستخدم اولا **")
    return await razan.edit(
        f"**▾∮المستخدم [{user.first_name}](tg://user?id={user.id})\n▾∮ تم رفعه في : {i} من المجموعات**"
    )

@lucmd9.on(admin_cmd(pattern="{down_admin} ?(.*)"))
async def gben(batt):
    dc = razan = batt
    i = 0
    sender = await dc.get_sender()
    me = await batt.client.get_me()
    await razan.edit("**▾∮ يتم تنزيل الشخص من رتبة الاشراف في جميع الكروبات**")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await batt.get_chat()
    if batt.is_private:
        user = batt.chat
        rank = batt.pattern_match.group(1)
    else:
        batt.chat.title
    try:
        user, rank = await get_full_user(batt)
    except:
        pass
    if me == user:
       lucmd9 = await razan.edit("▾∮ لا استطيع تنزيل نفسي 🧸🤍")
       return
    try:
        if not rank:
            rank = "ㅤㅤ"
    except:
        return await razan.edit(f"**▾∮ هنالك شي خطأ**")
    if user:
        telchanel = [d.entity.id
                     for d in await batt.client.get_dialogs()
                     if (d.is_group or d.is_channel)
                     ]
        rgt = ChatAdminRights(add_admins=None,
                               invite_users=None,
                                change_info=None,
                                 ban_users=None,
                                  delete_messages=None,
                                   pin_messages=None)
        for x in telchanel:
          try:
             await batt.client(EditAdminRequest(x, user, rgt, rank))
             i += 1
             await razan.edit(f"**▾∮ يتم تنزيله في **: `{i}` من المجموعات")
          except:
             pass
    else:
        await razan.edit(f"**▾∮ يجب عليك الرد على المستخدم اولا **")
    return await razan.edit(
        f"**▾∮المستخدم [{user.first_name}](tg://user?id={user.id})\n▾∮ تم تنزيله في : {i} من المجموعات**"
    )

CMD_HELP.update(
    {
        "اشراف عام": ".ارفع <بالرد ؏ شخص>\
\n لرفع المستخدم مشرف في جميع المجموعات ... \
\n\n.نزل <بالرد ؏ شخص>\n بالرد على الشخص لتنزيله من رتبة المشرف في جميع المجموعات"

    }
)
