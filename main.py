from services.scheduler_service import price_check_loop
from utils.input_validator import get_valid_target_price
import asyncio

target_price = get_valid_target_price()
asyncio.run(price_check_loop(target_price))