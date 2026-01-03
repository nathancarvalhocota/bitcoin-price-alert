from pycoingecko import CoinGeckoAPI
from services.telegram_service import send_telegram_message
CRYPTO_ID = 'bitcoin'

async def track_bitcoin_price(date):
    print(f"[TRACKER] Iniciando consulta do preço do Bitcoin ({date})")

    coin_gecko = CoinGeckoAPI()

    try:
        data = coin_gecko.get_price(ids=CRYPTO_ID, vs_currencies="usd")
        current_price = data.get(CRYPTO_ID, {}).get("usd")

        if current_price is None:
            print("[TRACKER] Preço não encontrado na resposta da API.")
            message = f"{date} - Não foi possível recuperar o preço do Bitcoin."
        else:
            print(f"[TRACKER] Preço atual obtido: ${current_price:,.2f} USD")
            message = f"{date} - Bitcoin: ${current_price:,.2f} USD"

    except Exception as e:
        print(f"[TRACKER][ERRO] Erro ao consultar a API do CoinGecko: {e}")
        message = f"{date} - Erro inesperado ao consultar o preço do Bitcoin."

   
    await send_telegram_message(message)

    
