from fastapi import FastAPI

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
@app.get("/user/123")
def read_user(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# Маршрут к странице пользователя с передачей данных в адресной строке
@app.get("/user")
def read_user_info(username: str="Ilya", age: int=24) ->dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}