import akinator
import asyncio
from telethon import events
import urllib.parse
from BATT import lucmd9
from ..core.managers import edit_or_reply
from datetime import datetime

plugin_category = "fun"
power = "🧞‍♂️"

ANSWER_TIMEOUT = 15

def progress_bar(progress_percentage):
    filled_blocks = int(progress_percentage * 10 / 100)
    empty_blocks = 10 - filled_blocks
    return "🟩" * filled_blocks + "⬛️" * empty_blocks  

@lucmd9.ar_cmd(
    pattern="اندرو$",
    command=("اندرو", plugin_category),
)
async def akinator_game(event):
    strongest= akinator.Akinator()
    current_question = strongest.start_game(language='ar')

    async with lucmd9.conversation(event.chat_id) as conv:
        progress_percentage = 0

        question_msg = await edit_or_reply(event,
            f"{current_question}\n\n"
            f"Level game: {progress_bar(progress_percentage)} {progress_percentage}%\n\n"
            f"Time wait: {ANSWER_TIMEOUT} sec\n\n"
            "Answer by :\n"
            "sure = نعم\n"
            "no = كلا\n"
            "idkoc = لا اعرف\n"
            "poss = يمكن\n"
            "cancel = انهاء اللعبة\n"
            "back = العودة"
        )

        try:
            response = await asyncio.wait_for(conv.wait_event(events.NewMessage(from_users=event.sender_id)), timeout=ANSWER_TIMEOUT)
            a = response.text
            await response.delete()
        except asyncio.TimeoutError:
            await question_msg.edit("Time is out.")
            return

        while strongest.progression <= 75:
            if a.lower() == "c":
                await question_msg.edit("Game canceled.")
                return
            elif a.lower() == "b":
                try:
                    current_question = strongest.back()
                except akinator.CantGoBackAnyFurther:
                    pass
            else:
                current_question = strongest.answer(a)

            progress_percentage = strongest.progression
            await question_msg.edit(
                f"{current_question}\n\n"
                f"Level game: {progress_bar(progress_percentage)} {progress_percentage}%\n\n"
                f"Time wait: {ANSWER_TIMEOUT} sec\n\n"
                "Answer by :\n"
                "sure = نعم\n"
                "no = لا\n"
                "idkoc = لا اعرف\n"
                "poss = من الممكن\n"
                "cancel = انهاء اللعبة\n"
                "back = العودة"
            )

            try:
                response = await asyncio.wait_for(conv.wait_event(events.NewMessage(from_users=event.sender_id)), timeout=ANSWER_TIMEOUT)
                a = response.text
                await response.delete()
            except asyncio.TimeoutError:
                await question_msg.edit("Time is out. Game ended.")
                return

        strongest.win()

        google = f"https://www.google.com/search?q={urllib.parse.quote_plus(strongest.first_guess['name'])}"

        copyright_message = f"\n\nCorner of Developer: DEV --> @lucmd9"

        correct = await edit_or_reply(event, f"Is he [{strongest.first_guess['name']}]({strongest.first_guess['absolute_picture_path']}) ({strongest.first_guess['description']})? am i right {power}{copyright_message}\n\nLevel game: {progress_percentage}%\n\n[Know more about {strongest.first_guess['name']}]({google})")
        response = await conv.wait_event(events.NewMessage(from_users=event.sender_id))
        if response.text.lower() in ["yes", "y", "نعم", "أجل"]:
            await correct.reply("Winner\n")
        else:
            await correct.reply("Loser\n")
