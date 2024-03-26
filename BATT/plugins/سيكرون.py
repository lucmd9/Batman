#امر تاخذ سكرين للمواقع
#————————BATT—————————-#LUC_MD9


import io
import traceback
from datetime import datetime
from selenium import webdriver
from telethon import events
from BATT import lucmd9
CHROME = "/usr/bin/google-chrome"

@lucmd9.ar_cmd(pattern="سكرن (.*)") #خوش غلطه هنا جانت
async def _(event):
    if event.fwd_from:
        return
    await event.edit("اصبر....")
    start = datetime.now()
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument("--test-type")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.binary_location = CHROME
        await event.edit("يتم تشغيل كوكل  bin")
        async with webdriver.Chrome(options=chrome_options) as driver:
            input_str = event.pattern_match.group(1)
            driver.get(input_str)
        await event.edit("يتم تجميع..")
        height = driver.execute_script("return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
        width = driver.execute_script("return Math.max(document.body.scrollWidth, document.body.offsetWidth, document.documentElement.clientWidth, document.documentElement.scrollWidth, document.documentElement.offsetWidth);")
        await event.edit("Painting web-page")
        driver.set_window_size(width + 100, height + 100)
        im_png = driver.get_screenshot_as_png()
        #هنا ينحفظ السكرين توضيح
        driver.close()
        await event.edit("يتم ايقاف كروم bin")
        message_id = event.message.id
        if event.reply_to_msg_id:
            message_id = event.reply_to_msg_id
        with io.BytesIO(im_png) as out_file:
            out_file.name = "BATT.screenCapture.PNG"
            await event.client.send_file(
                event.chat_id,
                out_file,
                caption=input_str,
                force_document=True,
                reply_to=message_id,
                allow_cache=False,
                silent=True
            )
        end = datetime.now()
        ms = (end - start).seconds
        await event.edit(f"تم التقاط السكرين استغرق حوالي {ms} sec")
    except Exception:
        await event.edit(traceback.format_exc())
      #جميع حقوق لسورس الخفاش تبوكه انيجك
