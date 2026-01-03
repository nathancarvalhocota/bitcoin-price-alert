from services.scheduler_service import price_check_loop
import asyncio

asyncio.run(price_check_loop())