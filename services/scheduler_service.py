from services.crypto_service import track_bitcoin_price
import asyncio
import datetime
from zoneinfo import ZoneInfo

# HORARIOS = ["06:00", "09:00", "12:00", "15:00", "18:00", "21:00"]
HORARIOS = ["13:15", "13:20", "13:25", "13:30", "18:00", "21:00"]
FUSO_BRASIL = ZoneInfo("America/Sao_Paulo")

async def price_check_loop(target_price):
    print("Iniciando o loop de verificação de preço...")
    while True:
        agora = datetime.datetime.now(FUSO_BRASIL).strftime("%H:%M")
        print(f"Horário verificado: {agora}")
        if agora in HORARIOS:
            print("Checando preço alvo...")
            try:
                await track_bitcoin_price(target_price, agora)
                print("Verificação concluída.")
            except Exception as e:
                print(f"Erro ao verificar preço: {e}")
            await asyncio.sleep(60) 
        await asyncio.sleep(5) 