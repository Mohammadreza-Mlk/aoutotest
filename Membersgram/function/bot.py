import requests 
BOT_TOKEN = '7829118396:AAHMoNEmBuH6JQ2fKT5uXzobYAHE87InZWM'
CHAT_ID = '@view10000posts1'
 
 
def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': message}
    try:
        requests.post(url, data=data)
    except:
        print("❌ ارسال پیام به تلگرام با خطا مواجه شد.")
