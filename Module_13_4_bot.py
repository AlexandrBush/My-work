from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

# Инициализация бота и диспетчера
API_TOKEN = '8162981162:AAFgTWjJqbVBoRe-Sm2Uxask-KDr8_BhCrc'
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Определение группы состояний
class UserState(StatesGroup):
    gender = State()
    age = State()
    growth = State()
    weight = State()


# Функция для начала цепочки
@dp.message_handler(commands=['calories'])
async def set_gender(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Мужской", "Женский")
    await message.answer('Выберите пол:', reply_markup=keyboard)
    await UserState.gender.set()


# Функция для обработки пола
@dp.message_handler(state=UserState.gender)
async def set_age(message: types.Message, state: FSMContext):
    gender = message.text
    await state.update_data(gender=gender)
    await message.answer('Введите свой возраст:', reply_markup=types.ReplyKeyboardRemove())
    await UserState.age.set()


# Функция для обработки возраста
@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


# Функция для обработки роста
@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


# Функция для обработки веса и вычисления нормы калорий
@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()

    age = data['age']
    growth = data['growth']
    weight = data['weight']
    gender = data['gender']

    if gender == "Мужской":
        # Формула Миффлина - Сан Жеора для мужчин
        calories = 10 * weight + 6.25 * growth - 5 * age + 5
    elif gender == "Женский":
        # Формула Миффлина - Сан Жеора для женщин
        calories = 10 * weight + 6.25 * growth - 5 * age - 161
    else:
        await message.answer("Неверный пол. Пожалуйста, начните снова.")
        await state.finish()
        return

    await message.answer(f'Ваша норма калорий: {calories:.2f} ккал в день.')
    await state.finish()


# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)