from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates  # Импортируем Jinja2Templates
from pydantic import BaseModel, constr, conint
from typing import List

app = FastAPI()

# Настройка Jinja2Templates
templates = Jinja2Templates(directory="templates")

# Модель пользователя
class User(BaseModel):
    id: int
    username: constr(min_length=1)  # Имя пользователя должно быть непустой строкой
    age: conint(gt=0, le=120)  # Возраст должен быть положительным числом и не превышать 120

# Пустой список пользователей
users: List[User] = []

# Валидация для user_id
def validate_user_id(user_id: int):
    if not isinstance(user_id, int) or user_id < 1 or user_id > 100:
        raise HTTPException(
            status_code=400,
            detail="Enter User ID. It must be an integer between 1 and 100."
        )
    return user_id

# Валидация для username
def validate_username(username: str):
    if not username or not isinstance(username, str) or len(username) < 1:
        raise HTTPException(
            status_code=400,
            detail="Enter a valid username. It must be a non-empty string."
        )
    return username

# Валидация для age
def validate_age(age: int):
    if not isinstance(age, int) or age <= 0 or age > 120:
        raise HTTPException(
            status_code=400,
            detail="Enter a valid age. It must be a positive integer between 1 and 120."
        )
    return age

# GET запрос для получения всех пользователей
@app.get('/', response_class=HTMLResponse)
def get_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

# GET запрос для получения конкретного пользователя
@app.get('/user/{user_id}', response_class=HTMLResponse)
def get_user(request: Request, user_id: int):
    user_id = validate_user_id(user_id)
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User was not found")

# POST запрос для добавления нового пользователя
@app.post('/user/{username}/{age}', response_model=User)
def add_user(username: str, age: int):
    # Валидация входных данных
    username = validate_username(username)
    age = validate_age(age)

    # Определяем id нового пользователя
    if not users:
        new_id = 1
    else:
        new_id = users[-1].id + 1

    # Создаем объект User
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user

# PUT запрос для обновления данных пользователя
@app.put('/user/{user_id}/{username}/{age}', response_model=User)
def update_user(user_id: int, username: str, age: int):
    # Валидация входных данных
    user_id = validate_user_id(user_id)
    username = validate_username(username)
    age = validate_age(age)

    # Ищем пользователя по id
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user

    # Если пользователь не найден
    raise HTTPException(status_code=404, detail="User was not found")

# DELETE запрос для удаления пользователя
@app.delete('/user/{user_id}', response_model=User)
def delete_user(user_id: int):
    # Валидация входных данных
    user_id = validate_user_id(user_id)

    # Ищем пользователя по id
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user

    # Если пользователь не найден
    raise HTTPException(status_code=404, detail="User was not found")