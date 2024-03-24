from BATT import lucmd9
from ..core.managers import edit_or_reply
from datetime import datetime
import random
from telethon import events
import emoji
import asyncio

plugin_category = "fun"



@lucmd9.on(events.NewMessage(pattern='.سباق'))
async def emoji_race(event):
    emojis = ["🍉", "🍎", "🍌", "🍇", "🍓", "🍍", "🍊", "🍐", "🍒", "🥝", "🥱", "😴", '🤤", "😪", "😵", "🤐", "🥴", "🤢", "🤮", "🤧", "😷", "🤒", "🤕", "🤑", "🤠", "😈", "👿", "👹", "👺", "🤡", "👻", "☠️" ,"👽", "👾", "🤖", "🎃", "😺", "😸", "😹", "😻", "😼", "😽", "🙀"
]
    race_Emoji = random.choice(emojis)
    Po = datetime.now()
    await edit_or_reply(event,f"اول واحد يرسل هذا الايموجي {race_Emoji} يربح نقطة!")

    async with lucmd9.conversation(event.chat_id) as conv:
        while True:
            response = await conv.wait_event(events.NewMessage(incoming=True, pattern=race_Emoji))
            if response.sender_id != event.sender_id:
                break

    race_end_time = datetime.now()
    time_taken = (race_end_time - Po).total_seconds()
    winner = await lucmd9.get_entity(response.sender_id)
    await response.reply(f"🎉 مبروك [{winner.first_name}](tg://user?id={winner.id}) \n- ثواني: {int(time_taken)} !!", parse_mode="md")
    

@lucmd9.on(events.NewMessage(pattern='.ايد'))
async def rock_paper_scissors(event):
    choices = {
        "حجرة": "ورقة",
        "ورقة": "مقص",
        "مقص": "حجرة"
    }
    user_choice = event.text.split()[-1]

    if user_choice not in choices:
        await edit_or_reply(event, "يرجى اختيار واحد من الخيارات التالية: حجرة، ورقة، أو مقص.")
        return

    bot_choice = random.choice(list(choices.keys()))
    if user_choice == bot_choice:
        result = "تعادل!"
    elif choices[bot_choice] == user_choice:
        result = "🎉 مبروك! لقد فزت."
    else:
        result = "😢 لقد خسرت. حاول مرة أخرى."

    await edit_or_reply(event, f"اختيارك: {user_choice}\nاختيار الساحر: {bot_choice}\nنتيجة اللعبة: {result}")





#بفلوسي

@lucmd9.on(events.NewMessage(pattern='.سيارات'))
async def car_race(event):
    racers = []
    Kk = None
    await edit_or_reply(event, "التسجيل بدأ ارسل 1 للانضمام")

    async with lucmd9.conversation(event.chat_id) as conv:
        while len(racers) < 5:
            response = await conv.wait_event(events.NewMessage(incoming=True, pattern="1"))
            if response.sender_id not in [r[0] for r in racers]:
                racer_entity = await lucmd9.get_entity(response.sender_id)
                racers.append((response.sender_id, racer_entity.username or racer_entity.first_name))
                Kk = await response.reply("تم التسجيل بنجاح")

    track = ["🏎️" for _ in range(5)]
    await Kk.edit(
        "السباق يبدأ الآن!\n" +
        "\n".join([f"{i+1}- {track[i]} [{racers[i][1]}](https://t.me/{racers[i][1]})" for i in range(5)])
    )

    for _ in range(10):
        await asyncio.sleep(1)
        moving_car = random.randint(0, 4)
        track[moving_car] = "-" + track[moving_car]
        await Kk.edit(
            "السباق يبدأ الآن!\n" + "\n".join([f"{i+1}- {track[i]} [{racers[i][1]}](https://t.me/{racers[i][1]})" for i in range(5)])
        )

    winner = racers[moving_car]
    await Kk.edit(
        f"🎉 مبروك [{winner[1]}](https://t.me/{winner[1]})! لقد فزت بالسباق!"
    )
    
#بالحظ
@lucmd9.ar_cmd(
    pattern="تحدي$",
    command=("تحدي", plugin_category),
    info={
        "header": "Challenge another user to a duel.",
        "description": "Randomly selects a winner between the challenger and the opponent.",
        "usage": "{tr}تحدي",
    },
)
async def challenge(event):
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "يرجى الرد على رسالة المستخدم الذي تريد تحديه.")
        return

    reply_message = await event.get_reply_message()
    opponent = reply_message.sender_id
    challenger = event.sender_id

    winner = random.choice([challenger, opponent])
    winner_entity = await lucmd9.get_entity(winner)

    await edit_or_reply(event, f"🎊 تهانينا [{winner_entity.first_name}](tg://user?id={winner})! لقد فزت في التحدي!")
    
    
#تكدر تضيف بعد وره ال plus
A_qq = [
    {"aW": "ما هو الحيوان الذي يمتلك أكبر عدد من الأسنان؟", "choices": ["التمساح", "القرش", "الفيل"], "Wa": "القرش"},
    {"aW": "ما هو العنصر الكيميائي الذي يرمز له بـ 'Au'؟", "choices": ["الذهب", "الفضة", "النحاس"], "Wa": "الذهب"},
    {"aW": "ما هي أكبر قارة في العالم؟", "choices": ["آسيا", "أفريقيا", "أوروبا"], "Wa": "آسيا"},
    {"aW": "من هو مؤلف رواية 'البؤساء'؟", "choices": ["فيكتور هوغو", "شارلز ديكنز", "ليو تولستوي"], "Wa": "فيكتور هوغو"},
    {"aW": "ما هي اللغة الرسمية للبرازيل؟", "choices": ["البرتغالية", "الإسبانية", "الإنجليزية"], "Wa": "البرتغالية"},
    {"aW": "ما هو أعمق محيط في العالم؟", "choices": ["المحيط الهادئ", "المحيط الأطلسي", "المحيط الهندي"], "Wa": "المحيط الهادئ"},
    {"aW": "من هو مخترع المصباح الكهربائي؟", "choices": ["توماس إديسون", "ألكسندر جراهام بيل", "نيكولا تسلا"], "Wa": "توماس إديسون"},
    {"aW": "ما هي عاصمة اليابان؟", "choices": ["طوكيو", "أوساكا", "كيوتو"], "Wa": "طوكيو"},
    {"aW": "من هو مؤلف كتاب 'الإخوان كارامازوف'؟", "choices": ["فيودور دوستويفسكي", "ليو تولستوي", "أنطون تشيخوف"], "Wa": "فيودور دوستويفسكي"},
    {"aW": "ما هو الطائر الذي يمكنه الطيران للخلف؟", "choices": ["الطنان", "النسر", "البومة"], "Wa": "الطنان"},
    {"aW": "ما هي أصغر دولة في العالم؟", "choices": ["الفاتيكان", "موناكو", "ناورو"], "Wa": "الفاتيكان"},
    {"aW": "ما هو أطول نهر في العالم؟", "choices": ["نهر النيل", "نهر الأمازون", "نهر يانغتسي"], "Wa": "نهر النيل"},
    {"aW": "من هو مؤلف مسرحية 'هاملت'؟", "choices": ["ويليام شكسبير", "سوفوكليس", "موليير"], "Wa": "ويليام شكسبير"},
    {"aW": "ما هو الكوكب الأصغر في المجموعة الشمسية؟", "choices": ["عطارد", "بلوتو", "المريخ"], "Wa": "عطارد"},
    {"aW": "من هو مؤلف رواية 'الحرب والسلام'؟", "choices": ["ليو تولستوي", "فيودور دوستويفسكي", "أنطون تشيخوف"], "Wa": "ليو تولستوي"},
    {"aW": "ما هو أقدم جامعة في العالم؟", "choices": ["جامعة القرويين", "جامعة بولونيا", "جامعة أكسفورد"], "Wa": "جامعة القرويين"},
    {"aW": "ما هو العنصر الكيميائي الذي يرمز له بـ 'O'؟", "choices": ["أكسجين", "أوزون", "أوسميوم"], "Wa": "أكسجين"},
    {"aW": "ما هي عملة اليابان؟", "choices": ["الين", "الوون", "اليوان"], "Wa": "الين"},
    {"aW": "من هو مؤلف مسرحية 'مكبث'؟", "choices": ["ويليام شكسبير", "كريستوفر مارلو", "بن جونسون"], "Wa": "ويليام شكسبير"},
    {"aW": "ما هو الحيوان الوطني لأستراليا؟", "choices": ["الكنغر", "الكوالا", "الإيمو"], "Wa": "الكنغر"},
    {"aW": "ما هي أكبر دولة في أفريقيا من حيث المساحة؟", "choices": ["الجزائر", "السودان", "ليبيا"], "Wa": "الجزائر"},
    {"aW": "ما هو أطول نفق في العالم؟", "choices": ["نفق سانت غوتارد", "نفق سيكان", "نفق لوشبرغ"], "Wa": "نفق سانت غوتارد"},
    {"aW": "ما هي أكبر جزيرة في العالم؟", "choices": ["غرينلاند", "نيو غينيا", "بورنيو"], "Wa": "غرينلاند"},
    {"aW": "من هو مؤلف كتاب 'الأمير'؟", "choices": ["نيكولو مكيافيلي", "توماس هوبز", "جون لوك"], "Wa": "نيكولو مكيافيلي"},
    {"aW": "ما هي الدولة التي تضم مدينة البندقية؟", "choices": ["إيطاليا", "فرنسا", "إسبانيا"], "Wa": "إيطاليا"},
    {"aW": "من هو مخترع الراديو؟", "choices": ["غوليلمو ماركوني", "نيكولا تسلا", "ألكسندر جراهام بيل"], "Wa": "غوليلمو ماركوني"},
    {"aW": "ما هي عاصمة كندا؟", "choices": ["أوتاوا", "تورونتو", "مونتريال"], "Wa": "أوتاوا"},
    {"aW": "ما هو أقدم علم في العالم؟", "choices": ["علم الرياضيات", "علم الفلك", "علم الكيمياء"], "Wa": "علم الفلك"},
    {"aW": "ما هي أصغر دولة في أفريقيا؟", "choices": ["سيشيل", "غامبيا", "موريشيوس"], "Wa": "سيشيل"},
    {"aW": "ما هو البركان الأكثر نشاطاً في العالم؟", "choices": ["كيلاويا", "إتنا", "فيزوف"], "Wa": "كيلاويا"},
    {"aW": "ما هي اللغة الرسمية للأرجنتين؟", "choices": ["الإسبانية", "البرتغالية", "الإنجليزية"], "Wa": "الإسبانية"},
    {"aW": "ما هو العنصر الكيميائي الذي يرمز له بـ 'Fe'؟", "choices": ["الحديد", "الفلور", "الفرانسيوم"], "Wa": "الحديد"},
    {"aW": "ما هي عاصمة جنوب أفريقيا؟", "choices": ["بريتوريا", "كيب تاون", "جوهانسبرغ"], "Wa": "بريتوريا"},
    {"aW": "من هو مؤلف كتاب 'الأخوة كارامازوف'؟", "choices": ["فيودور دوستويفسكي", "ليو تولستوي", "أنطون تشيخوف"], "Wa": "فيودور دوستويفسكي"},
    {"aW": "ما هو الحيوان الذي يعيش أطول عمراً؟", "choices": ["السلحفاة", "الفيل", "الببغاء"], "Wa": "السلحفاة"},
    {"aW": "ما هو أصغر كوكب في المجموعة الشمسية؟", "choices": ["عطارد", "بلوتو", "المريخ"], "Wa": "عطارد"},
    {"aW": "ما هي اللغة الرسمية لمصر؟", "choices": ["العربية", "الإنجليزية", "الفرنسية"], "Wa": "العربية"},
    {"aW": "من هو مؤلف كتاب 'الجمهورية'؟", "choices": ["أفلاطون", "أرسطو", "سقراط"], "Wa": "أفلاطون"},
    {"aW": "ما هي عاصمة الهند؟", "choices": ["نيودلهي", "مومباي", "بنغالور"], "Wa": "نيودلهي"}
]

qq = [
    {"aW": "ما هو أطول نهر في العالم؟", "choices": ["النيل", "الأمازون", "المسيسيبي"], "Wa": "الأمازون"},
    {"aW": "من هو مؤلف رواية 'البؤساء'؟", "choices": ["فيكتور هوغو", "تشارلز ديكنز", "ليو تولستوي"], "Wa": "فيكتور هوغو"},
    {"aW": "كم عدد الكواكب في نظامنا الشمسي؟", "choices": ["8", "9", "10"], "Wa": "8"},
]



@lucmd9.ar_cmd(
    pattern="المليون$",
    command=("المليون", plugin_category),
    info={
        "header": "Play a million game.",
        "description": "لعبه مثل مال من سيربح المليون",
        "usage": "{tr}المليون",
    },
)
async def million(event):
    Bq = qq + A_qq
    aW = random.choice(Bq)
    choices = aW["choices"][:]
    random.shuffle(choices)
    choices_text = "\n".join([f"{i+1}. {choice}" for i, choice in enumerate(choices)])
    await edit_or_reply(event, f"{aW['aW']}\n\n{choices_text}\n\nاكتب رقم الإجابة الصحيحة:")

    async with lucmd9.conversation(event.chat_id) as conv:
        response = await conv.wait_event(events.NewMessage(pattern=r'^[1-3]$', from_users=event.sender_id))
        Wa_index = int(response.text) - 1
        if choices[Wa_index] == aW["Wa"]:
            await response.edit("🎉 صحيح! إجابتك صحيحة.")
        else:
            await response.edit(f"❌ خطأ! الإجابة الصحيحة هي: {aW['Wa']}")


# قائمة الإيموجيات مع الأعلام 
emojis = {
    "🇸🇦": "السعودية",
    "🇦🇪": "الإمارات",
    "🇪🇬": "مصر",
    "🇶🇦": "قطر",
    "🇴🇲": "عُمان",
    "🇧🇭": "البحرين",
    "🇰🇼": "الكويت",
    "🇯🇴": "الأردن",
    "🇱🇧": "لبنان",
    "🇵🇸": "فلسطين",
    "🇾🇪": "اليمن",
    "🇮🇶": "العراق",
    "🇹🇳": "تونس",
    "🇩🇿": "الجزائر",
    "🇲🇦": "المغرب",
    "🇱🇾": "ليبيا",
    "🇸🇩": "السودان",
    "🇸🇾": "سوريا",
    "🇯🇵": "اليابان",
    "🇰🇷": "كوريا الجنوبية",
    "🇨🇳": "الصين",
    "🇮🇳": "الهند",
    "🇵🇰": "باكستان",
    "🇮🇩": "إندونيسيا",
    "🇲🇾": "ماليزيا",
    "🇹🇭": "تايلاند",
    "🇵🇭": "الفلبين",
    "🇻🇳": "فيتنام",
    "🇰🇼": "كويت",
    "🇲🇻": "المالديف",
    "🇧🇩": "بنغلاديش",
    "🇦🇫": "أفغانستان",
    "🇹🇷": "تركيا",
    "🇮🇷": "إيران",
    "🇷🇺": "روسيا",
    "🇺🇦": "أوكرانيا",
    "🇩🇪": "ألمانيا",
    "🇫🇷": "فرنسا",
    "🇬🇧": "المملكة المتحدة",
    "🇮🇹": "إيطاليا",
    "🇪🇸": "إسبانيا",
    "🇵🇱": "بولندا",
    "🇳🇱": "هولندا",
    "🇧🇪": "بلجيكا",
    "🇦🇹": "النمسا",
    "🇨🇭": "سويسرا",
    "🇬🇷": "اليونان",
    "🇵🇹": "البرتغال",
    "🇸🇪": "السويد",
    "🇩🇰": "الدنمارك",
    "🇫🇮": "فنلندا",
    "🇳🇴": "النرويج",
    "🇮🇸": "آيسلندا",
    "🇮🇪": "أيرلندا",
    "🇱🇺": "لوكسمبورغ",
    "🇫🇴": "جزر فارو",
    "🇲🇨": "موناكو",
    "🇲🇹": "مالطا",
    "🇻🇦": "الفاتيكان",
} 
@lucmd9.on(events.NewMessage(pattern='.اعلام'))
async def flag_race(event):
    
    flag_Emoji, country = random.choice(list(emojis.items()))
    Po = datetime.now()
    await edit_or_reply(event, f"اول واحد يرسل العلم {flag_Emoji} لـ {country} يربح نقطة!")

    async with lucmd9.conversation(event.chat_id) as conv:
        while True:
            response = await conv.wait_event(events.NewMessage(incoming=True, pattern=flag_Emoji))
            if response.sender_id != event.sender_id:
                break

    race_end_time = datetime.now()
    time_taken = (race_end_time - Po).total_seconds()
    winner = await lucmd9.get_entity(response.sender_id)
    await response.reply(f"🎉 حب مبروك [{winner.first_name}](tg://user?id={winner.id}) \n- ثواني: {int(time_taken)} !!", parse_mode="md")
#جميع الحقوق لهذا الأمر لسورس الخفاش

# قائمة العواصم مع الدول العربية
capitals = {
    "السعودية": "الرياض",
    "الإمارات": "أبوظبي",
    "مصر": "القاهرة",
    "قطر": "الدوحة",
    "عمان": "مسقط",
    "البحرين": "المنامة",
    "الأردن": "عمان",
    "لبنان": "بيروت",
    "فلسطين": "القدس",
    "اليمن": "صنعاء",
    "العراق": "بغداد",
    # يمكنك إضافة المزيد من العواصم والدول هنا
}

@lucmd9.on(events.NewMessage(pattern='.عواصم'))
async def capital_race(event):
    # اختيار عشوائي لاسم الدولة والعاصمة
    country, capital = random.choice(list(capitals.items()))
    start_time = datetime.now()
    await edit_or_reply(event, f"اول واحد يقول ما اسم عاصمة {country}؟")

    async with lucmd9.conversation(event.chat_id) as conv:
        response = await conv.wait_event(events.NewMessage(incoming=True, from_users=event.chat_id))

    end_time = datetime.now()
    time_taken = (end_time - start_time).total_seconds()
    if response.text.strip().lower() == capital.lower():
        winner = await lucmd9.get_entity(response.sender_id)
        await response.reply(f"🎉 مبروك [{winner.first_name}](tg://user?id={winner.id}) \n- ثواني: {int(time_taken)} !!", parse_mode="md")
    else:
        await response.reply("للأسف، الإجابة غير صحيحة.")
