from fastapi import APIRouter, Depends, status, HTTPException
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from app.backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from app.models import *
from app.schemas import CreateUser, UpdateUser
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/")
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users

@router.get('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is not None:
        return user
    else:
        raise HTTPException(status_code=404, detail="User was not found")

@router.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], create_user_model: CreateUser):
    db.execute(insert(User).values(
        username=create_user_model.username,
        firstname=create_user_model.firstname,
        lastname=create_user_model.lastname,
        age=create_user_model.age,
        slug=slugify(create_user_model.username)
    ))
    db.commit()
    return {
        "status_code": status.HTTP_201_CREATED,
        "transaction": "User create is successful"
    }

@router.put("/update")
async def update_user(db: Annotated[Session, Depends(get_db)], update_model: UpdateUser, user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is not None:
        db.execute(update(User).where(User.id == user_id).values(
            username=update_model.username,
            firstname=update_model.firstname,
            lastname=update_model.lastname,
            age=update_model.age,
            slug=slugify(update_model.username)
        ))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful'}
    raise HTTPException(status_code=404, detail="User was not found")

@router.delete("/delete")
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is not None:
        db.execute(delete(User).where(User.id == user_id))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'User delete is successful'}
    raise HTTPException(status_code=404, detail="User was not found")