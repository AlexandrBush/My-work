from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "8162981162:AAFgTWjJqbVBoRe-Sm2Uxask-KDr8_BhCrc"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(text=['Urban', 'ff'])
async def urban_message(message):
    await message.answer('Urbanan mesage')

@dp.message_handler(commands=['Start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Рады вас видеть, чем можем помочь?')

@dp.message_handler()
async def all_message(message):
    await message.answer("Введите команду /start, чтобы начать общение")
    await message.answer(message.text.upper())

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)