'''
Цель: выработать навык работы с CRUD запросами.

Задача "Имитация работы с БД":
Создайте новое приложение FastAPI и сделайте CRUD запросы.
Создайте словарь users = {'1': 'Имя: Example, возраст: 18'}
Реализуйте 4 CRUD запроса:
get запрос по маршруту '/users', который возвращает словарь users.
post запрос по маршруту '/user/{username}/{age}', который добавляет в словарь по максимальному по значению ключом значение строки "Имя: {username}, возраст: {age}". И возвращает строку "User <user_id> is registered".
put запрос по маршруту '/user/{user_id}/{username}/{age}', который обновляет значение из словаря users под ключом user_id на строку "Имя: {username}, возраст: {age}". И возвращает строку "The user <user_id> is updated"
delete запрос по маршруту '/user/{user_id}', который удаляет из словаря users по ключу user_id пару.
Выполните каждый из этих запросов по порядку. Ответы должны совпадать:
1. GET '/users'
{
"1": "Имя: Example, возраст: 18"
}
2. POST '/user/{username}/{age}' # username - UrbanUser, age - 24
"User 2 is registered"
3. POST '/user/{username}/{age}' # username - NewUser, age - 22
"User 3 is registered"
4. PUT '/user/{user_id}/{username}/{age}' # user_id - 1, username - UrbanProfi, age - 28
"User 1 has been updated"
5. DELETE '/user/{user_id}' # user_id - 2
"User 2 has been deleted"
6. GET '/users'
{
"1": "Имя: UrbanProfi, возраст: 28",
"3": "Имя: NewUser, возраст: 22"
}

Примечания:
Не забудьте написать валидацию для каждого запроса, аналогично предыдущему заданию.
'''

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr, conint

app = FastAPI()

# Инициализация словаря users
users = {
    '1': 'Имя: Example, возраст: 18'
}

# Модель данных для пользователя
class User(BaseModel):
    username: constr(min_length=1)  # Имя пользователя должно быть не пустым
    age: conint(ge=0)  # Возраст должен быть неотрицательным целым числом

# GET запрос для получения всех пользователей
@app.get('/users')
def get_users():
    return users

# POST запрос для добавления нового пользователя
@app.post('/user/{username}/{age}')
def add_user(username: str, age: int):
    # Валидация данных
    user = User(username=username, age=age)

    # Находим максимальный ключ
    max_id = max(map(int, users.keys()), default=0)
    new_id = str(max_id + 1)
    users[new_id] = f"Имя: {user.username}, возраст: {user.age}"
    return {"message": f"User {new_id} is registered"}

# PUT запрос для обновления данных пользователя
@app.put('/user/{user_id}/{username}/{age}')
def update_user(user_id: str, username: str, age: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    # Валидация данных
    user = User(username=username, age=age)

    users[user_id] = f"Имя: {user.username}, возраст: {user.age}"
    return {"message": f"User {user_id} has been updated"}

# DELETE запрос для удаления пользователя
@app.delete('/user/{user_id}')
def delete_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return {"message": f"User {user_id} has been deleted"}
