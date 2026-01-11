import asyncio
from fastapi import FastAPI
from api.routes import router
from services.scheduler_service import price_check_loop 

app = FastAPI(title="Crypto Price Bot API")

app.include_router(router)

@app.on_event("startup")
async def startup():
    asyncio.create_task(price_check_loop())
