from fastapi import APIRouter, HTTPException
from models.crypto import CryptoRequest
from services.state_service import set_crypto
from services.state_service import get_crypto
router = APIRouter()

@router.post("/crypto")
def change_crypto(body: CryptoRequest):
    if not body.crypto.strip():
        raise HTTPException(status_code=400, detail="Crypto inválida")

    set_crypto(body.crypto)
    return {"message": "Criptomoeda atualizada"}

@router.get("/crypto")
def check_crypto():
    return {"crypto": get_crypto()}