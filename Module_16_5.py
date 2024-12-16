from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, constr, conint, ValidationError
from typing import Annotated, List

app = FastAPI()

# Настройка Jinja2Templates
templates = Jinja2Templates(directory="templates")

# Модель пользователя
class User(BaseModel):
    id: int
    username: Annotated[str, constr(min_length=1)]  # Имя пользователя должно быть непустой строкой
    age: Annotated[int, conint(gt=0, le=120)]  # Возраст должен быть положительным числом и не превышать 120

# Пустой список пользователей
users: List[User] = []

# Аннотации для валидации входных параметров
UserId = Annotated[int, conint(gt=0, le=100)]
Username = Annotated[str, constr(min_length=1)]
Age = Annotated[int, conint(gt=0, le=120)]

# GET запрос для получения всех пользователей
@app.get('/', response_class=HTMLResponse)
def get_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

# GET запрос для получения конкретного пользователя
@app.get('/user/{user_id}', response_class=HTMLResponse)
def get_user(request: Request, user_id: UserId):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User was not found")

# POST запрос для добавления нового пользователя
@app.post('/user/{username}/{age}', response_model=User)
def add_user(username: Username, age: Age):
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
def update_user(user_id: UserId, username: Username, age: Age):
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
def delete_user(user_id: UserId):
    # Ищем пользователя по id
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user

    # Если пользователь не найден
    raise HTTPException(status_code=404, detail="User was not found")
