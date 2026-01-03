from telegram import Bot
from dotenv import load_dotenv
import os

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

async def send_telegram_message(message: str):
    print("[TELEGRAM] Enviando mensagem...")

    try:
        bot = Bot(token=TELEGRAM_BOT_TOKEN)       
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
        print("[TELEGRAM] Mensagem enviada com sucesso.")

    except Exception as e:
        print(f"[TELEGRAM][ERRO] Falha ao enviar mensagem: {e}")