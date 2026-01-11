from pycoingecko import CoinGeckoAPI
from services.telegram_service import send_telegram_message
from services.state_service import get_crypto
from services.validator_service import validate_crypto_id

async def track_price(date):
    CRYPTO_ID = get_crypto()
    print(f"[TRACKER] Iniciando consulta do preço de {CRYPTO_ID} ({date})")

    try:
        coin_gecko = CoinGeckoAPI()
        data = coin_gecko.get_price(ids=CRYPTO_ID, vs_currencies="usd")
        current_price = data.get(CRYPTO_ID, {}).get("usd")

        if current_price is None:
            print("[TRACKER] Preço não encontrado na resposta da API.")
            message = f"{date} - Não foi possível recuperar o preço de {CRYPTO_ID}."
        else:
            print(f"[TRACKER] Preço atual obtido: ${current_price:,.2f} USD")
            message = f"{date} - {CRYPTO_ID}: ${current_price:,.2f} USD"

    except Exception as e:
        print(f"[TRACKER][ERRO] Erro ao consultar a API do CoinGecko: {e}")
        message = f"{date} - Erro inesperado ao consultar o preço de {CRYPTO_ID}."
   
    await send_telegram_message(message)

    
