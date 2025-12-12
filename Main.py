import telebot
import random
import string
import time
import os

TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

bot = telebot.TeleBot(TOKEN)

def gen():
    chars = string.ascii_lowercase + string.digits  # بدون underscore عشان يطلع يوزرات أنظف
    while True:
        length = random.choice([4, 5])
        u = ''.join(random.choice(chars) for _ in range(length))
        if not u[0].isdigit():  # ما يبدأش برقم
            return '@' + u

while True:
    try:
        username = gen()
        bot.get_chat(username)  # لو نجح = محجوز
        print(f"{username} ← محجوز")
        
    except telebot.apihelper.ApiTelegramException as e:
        if e.error_code == 400:
            msg = f"""
يوزر نادر طلع دلوقتي!!

{username}

احجزه فورًا من الإعدادات → Username قبل ما حد ياخده!
            """
            bot.send_message(CHAT_ID, msg)
            print(f"تم الإرسال → {username}")
            
    except Exception as e:
        print("خطأ:", e)
        
    time.sleep(6)  # 6 ثواني بين كل محاولة
