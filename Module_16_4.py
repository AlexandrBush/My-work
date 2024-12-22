'''
Цель: научиться описывать и использовать Pydantic модель.

Задача "Модель пользователя":
Подготовка:
Используйте CRUD запросы из предыдущей задачи.
Создайте пустой список users = []
Создайте класс(модель) User, наследованный от BaseModel, который будет содержать следующие поля:
id - номер пользователя (int)
username - имя пользователя (str)
age - возраст пользователя (int)

Измените и дополните ранее описанные 4 CRUD запроса:
get запрос по маршруту '/users' теперь возвращает список users.
post запрос по маршруту '/user/{username}/{age}', теперь:
Добавляет в список users объект User.
id этого объекта будет на 1 больше, чем у последнего в списке users. Если список users пустой, то 1.
Все остальные параметры объекта User - переданные в функцию username и age соответственно.
В конце возвращает созданного пользователя.
put запрос по маршруту '/user/{user_id}/{username}/{age}' теперь:
Обновляет username и age пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.
delete запрос по маршруту '/user/{user_id}', теперь:
Удаляет пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.
Выполните каждый из этих запросов по порядку. Ответы должны совпадать:
1. GET '/users'
[]
2. POST '/user/{username}/{age}' # username - UrbanUser, age - 24

3. POST '/user/{username}/{age}' # username - UrbanTest, age - 36

4. POST '/user/{username}/{age}' # username - Admin, age - 42

5. PUT '/user/{user_id}/{username}/{age}' # user_id - 1, username - UrbanProfi, age - 28

6. DELETE '/user/{user_id}' # user_id - 2

7. GET '/users'

8. DELETE '/user/{user_id}' # user_id - 2



'''
from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, Field
from typing import List, Annotated

app = FastAPI()

# Модель пользователя
class User(BaseModel):
    id: int
    username: str = Field(min_length=1, description="Имя пользователя должно быть непустой строкой")
    age: int = Field(gt=0, le=120, description="Возраст должен быть положительным числом и не превышать 120")

# Пустой список пользователей
users: List[User] = []

# GET запрос для получения всех пользователей
@app.get('/users', response_model=List[User])
def get_users():
    return users

# GET запрос для получения пользователя по ID
@app.get("/user/{user_id}")
def read_user(
    user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example=45)]
):
    # Ищем пользователя по ID
    for user in users:
        if user.id == user_id:
            return user

    # Если пользователь не найден
    raise HTTPException(status_code=404, detail="User was not found")

# GET запрос для получения пользователя по username и age
@app.get("/user/{username}/{age}")
def read_user_info(
    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="Nastya")],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=45)]
):
    # Ищем пользователя по username и age
    for user in users:
        if user.username == username and user.age == age:
            return user

    # Если пользователь не найден
    raise HTTPException(status_code=404, detail="User was not found")

# POST запрос для добавления нового пользователя
@app.post('/user/{username}/{age}', response_model=User)
def add_user(
    username: Annotated[str, Path(min_length=1, description="Username must be at least 1 character long")],
    age: Annotated[int, Path(gt=0, le=120, description="Age must be between 1 and 120")]
):
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
def update_user(
    user_id: Annotated[int, Path(ge=1, le=100, description="User ID must be between 1 and 100")],
    username: Annotated[str, Path(min_length=1, description="Username must be at least 1 character long")],
    age: Annotated[int, Path(gt=0, le=120, description="Age must be between 1 and 120")]
):
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
def delete_user(
    user_id: Annotated[int, Path(ge=1, le=100, description="User ID must be between 1 and 100")]
):
    # Ищем пользователя по id
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user

    # Если пользователь не найден
    raise HTTPException(status_code=404, detail="User was not found")
