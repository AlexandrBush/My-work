from fastapi import FastAPI, Path, Query, HTTPException
from typing import Annotated

# Создание объекта FastAPI
app = FastAPI()

# Маршрут к главной странице
@app.get("/")
def read_root():
    return {"message": "Главная страница"}

# Маршрут к странице администратора
@app.get("/user/admin")
def read_admin():
    return {"message": "Вы вошли как администратор"}

# Маршрут к страницам пользователей с параметром в пути
@app.get("/user/{user_id}")
def read_user(
    user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example=45)]
):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# Маршрут к странице пользователя с передачей данных в адресной строке
@app.get("/user/{username}/{age}")
def read_user_info(
    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="Nastya")],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=45)]
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}