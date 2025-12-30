from pycoingecko import CoinGeckoAPI
from services.telegram_service import send_telegram_message
CRYPTO_ID = 'bitcoin'

async def track_bitcoin_price(target_price, date):
    coin_gecko = CoinGeckoAPI()
    message = f"Falha ao recuperar o preço do Bitcoin às {date}."
    data = coin_gecko.get_price(ids=CRYPTO_ID, vs_currencies='usd')
    current_price = data.get(CRYPTO_ID, {}).get('usd', 'Preço não encontrado')
    if current_price != 'Preço não encontrado':
        if float(current_price) >= float(target_price):
            message = f"Bitcoin está acima ou igual ao seu valor alvo de ${target_price}. Valor atual (USD): ${current_price}"
        else:
            message = f"Bitcoin está abaixo do seu valor alvo de ${target_price}. Valor atual (USD): ${current_price}"
    print("Enviando mensagem via Telegram...")
    await send_telegram_message(message)
    
