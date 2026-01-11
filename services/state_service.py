from threading import Lock

_current_crypto = "bitcoin"
_lock = Lock()

def get_crypto() -> str:
    with _lock:
        return _current_crypto

def set_crypto(new_crypto: str):
    global _current_crypto
    with _lock:
        _current_crypto = new_crypto.lower()
