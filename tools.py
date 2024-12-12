from datetime import timedelta, datetime, timezone

from settings import settings

import jwt

data = {"sub": "JohnDou", "id": 1}


def create_token(data: dict):
    data.update({
        "exp": datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MIN)
    })
    encoded_jwt = jwt.encode(data, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def decode_token(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError as e:
        print(f"Token has expired: {e}")
        return False
    except jwt.PyJWTError as e:
        print(f"Error: token not decode: {e}")
        return False
