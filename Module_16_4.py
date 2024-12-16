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
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr, conint
from typing import List

app = FastAPI()

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
@app.get('/users', response_model=List[User])
def get_users():
    return users

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
