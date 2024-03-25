import akinator
import asyncio
from telethon import events
import urllib.parse

# الأيموجي 
EMOJI = "🧞‍♂️"

# مدة الوقت المحدد للإجابة في ثواني
ANSWER_TIMEOUT = 30

@lucmd9.ar_cmd(
    pattern="المارد$",
    command=("المارد", plugin_category),
    info={
        "header": "امر المارد  .",
        "description": "مكتبة المارد  ا .",
        "usage": "{tr}المارد",
    },
)
async def akinator_game(event):
    game = akinator.Akinator()
    current_question = game.start_game(language='ar')

    async with Qrh9.conversation(event.chat_id) as conv:
        progress_percentage = 0
        progress_bar = "[" + "=" * int(progress_percentage * 0.5) + ">" + " " * (50 - int(progress_percentage * 0.5)) + "]"

        question_msg = await edit_or_reply(event,
            f"{current_question}\n\n"
            f"تقدم اللعبة: {progress_bar} {progress_percentage}%\n\n"
            f"وقت الانتظار للإجابة: {ANSWER_TIMEOUT} ثانية\n\n"
            "اجب ب:\n"
            "`y` = نعم\n"
            "`n` = لا\n"
            "`idk` = لا اعلم\n"
            "`p` = من الممكن\n"
            "`c` = انهاء اللعبة\n"
            "`b` = رجوع"
        )

        try:
            response = await asyncio.wait_for(conv.wait_event(events.NewMessage(from_users=event.sender_id)), timeout=ANSWER_TIMEOUT)
            a = response.text
            await response.delete()
        except asyncio.TimeoutError:
            await question_msg.edit("لقد انتهى الوقت المحدد للإجابة. تم إنهاء اللعبة.")
            return

        while game.progression <= 80:
            if a.lower() == "c":
                await question_msg.edit("لقد ألغيت اللعبة.")
                return
            elif a.lower() == "b":
                try:
                    current_question = game.back()
                except akinator.CantGoBackAnyFurther:
                    pass
            else:
                current_question = game.answer(a)

            progress_percentage = game.progression
            progress_bar = "[" + "=" * int(progress_percentage * 0.5) + ">" + " " * (50 - int(progress_percentage * 0.5)) + "]"

            await question_msg.edit(
                f"{current_question}\n\n"
                f"تقدم اللعبة: {progress_bar} {progress_percentage}%\n\n"
                f"وقت الانتظار للإجابة: {ANSWER_TIMEOUT} ثانية\n\n"
                "اجب ب:\n"
                "`y` = نعم\n"
                "`n` = لا\n"
                "`idk` = لا اعلم\n"
                "`p` = من الممكن\n"
                "`c` = انهاء اللعبة\n"
                "`b` = رجوع"
            )

            try:
                response = await asyncio.wait_for(conv.wait_event(events.NewMessage(from_users=event.sender_id)), timeout=ANSWER_TIMEOUT)
                a = response.text
                await response.delete()
            except asyncio.TimeoutError:
                await question_msg.edit("لقد انتهى الوقت المحدد للإجابة. تم إنهاء اللعبة.")
                return

        game.win()

        # توليد رابط Google لمعرفة معلومات الشخصية
        google_search_url = f"https://www.google.com/search?q={urllib.parse.quote_plus(game.first_guess['name'])}"

        # إضافة حقوقك بنهاية السؤال
        copyright_message = f"\n\nحقوق البرمجة: DEV --> @lucmd9"

        correct = await edit_or_reply(event, f"هل هو [{game.first_guess['name']}]({game.first_guess['absolute_picture_path']}) ({game.first_guess['description']})؟ هل كنت محقًا؟{EMOJI}{copyright_message}\n\nتقدم اللعبة: {progress_percentage}%\n\n[تعرف على المزيد عن {game.first_guess['name']}]({google_search_url})")
        response = await conv.wait_event(events.NewMessage(from_users=event.sender_id))
        if response.text.lower() in ["yes", "y", "نعم", "أجل"]:
            await correct.reply("ياي\n")
        else:
            await correct.reply("أوف\n")
