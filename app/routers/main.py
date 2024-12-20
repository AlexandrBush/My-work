from fastapi import FastAPI
from routers.task import router as task_router
from routers.user import router as user_router

app = FastAPI()

# Подключаем маршруты
app.include_router(task_router)
app.include_router(user_router)

# Основной маршрут
@app.get("/")
def read_root():
    return {"message": "Welcome to Taskmanager"}