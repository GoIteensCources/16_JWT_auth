import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from werkzeug.security import check_password_hash

from db import fake_users_db
from tools import create_token, decode_token


app = FastAPI(docs_url="/")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


@app.post("/token")
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users_db.get(form_data.username)

    if not user:
        raise HTTPException(status_code=400, detail="Username or Password incorrect")

    if not check_password_hash(user["hashed_password"], form_data.password):
        raise HTTPException(status_code=400, detail="Username or Password incorrect")

    token = create_token(data={"username": user["username"], "id": 1})
    return {"access_token": token, "token_type": "bearer"}


async def get_current_user(token: str = Depends(oauth2_scheme)):

    user_data = decode_token(token)
    if not user_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Невірний токен",
            headers={"Authorization": "Bearer"},
        )
    return user_data


@app.get("/item")
async def get_item(user=Depends(get_current_user)):
    return {"data": user}

@app.get("/item_for_admin")
async def get_item(user.......):
    return {"data": user, "mess": "only for admin"}

if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", reload=True)
