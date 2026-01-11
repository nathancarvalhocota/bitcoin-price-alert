from pycoingecko import CoinGeckoAPI
from services.telegram_service import send_telegram_message
from services.state_service import get_crypto 

async def validate_crypto_id():
    coin_gecko = CoinGeckoAPI()
    CRYPTO_ID = get_crypto()
    data = coin_gecko.get_price(ids=CRYPTO_ID, vs_currencies="usd")
    current_price = data.get(CRYPTO_ID, {}).get("usd")
    
    if current_price is None:
        raise InvalidCryptoException(f"Crypto inválida ou não encontrada no CoinGecko: {CRYPTO_ID}")
            