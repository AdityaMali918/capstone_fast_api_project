from datetime import datetime, timedelta, timezone
from authlib import jwt, JWTError
from app.core.config import settings 

def create_token(data: dict):
    header = {'alg': settings.hash_algorithm}
    expire = datetime.now(timezone.utc) + timedelta(minutes=int(settings.access_token_expiry_minutes))
    payload = data.copy()
    payload.update({"exp":expire})
    return jwt.encode(header, payload, settings.secret_key)


def verify_token(token: str):
    try:
        payload = jwt.decode(token, settings.secret_key)
        payload.validate()
        return payload
    except JWTError:
        return None    