from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

# Импортируем функции из crud_functions.py
from crud_functions import initiate_db, get_all_products, add_user, is_included

# Инициализация бота и диспетчера
API_TOKEN = '###'
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Инициализация базы данных
initiate_db()

# Определение группы состояний
class UserState(StatesGroup):
    gender = State()
    age = State()
    growth = State()
    weight = State()

# Определение группы состояний для регистрации
class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()

# Функция для начала цепочки
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton('Рассчитать'), types.KeyboardButton('Информация'), types.KeyboardButton('Купить'), types.KeyboardButton('Регистрация'))
    await message.answer('Выберите действие:', reply_markup=keyboard)

# Функция для отправки Inline-клавиатуры
@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def main_menu(message: types.Message):
    inline_keyboard = types.InlineKeyboardMarkup()
    inline_keyboard.add(types.InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories'))
    inline_keyboard.add(types.InlineKeyboardButton('Формулы расчёта', callback_data='formulas'))
    await message.answer('Выберите опцию:', reply_markup=inline_keyboard)

# Функция для отправки информации о боте
@dp.message_handler(lambda message: message.text == 'Информация')
async def bot_info(message: types.Message):
    info = (
        "Этот бот помогает рассчитать вашу суточную норму калорий по формуле Миффлина-Сан Жеора.\n\n"
        "Для расчета нормы калорий нажмите кнопку 'Рассчитать' и следуйте инструкциям.\n\n"
        "Разработчик: AlexBush"
    )
    await message.answer(info)

# Функция для отправки формул расчета калорий
@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    formulas = (
        "Формула Миффлина-Сан Жеора для мужчин:\n"
        "10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) + 5\n\n"
        "Формула Миффлина-Сан Жеора для женщин:\n"
        "10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) - 161"
    )
    await call.message.answer(formulas)
    await call.answer()

# Функция для начала цепочки расчета калорий
@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_gender(call: types.CallbackQuery):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Мужской", "Женский")
    await call.message.answer('Выберите пол:', reply_markup=keyboard)
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

    # Возвращение в меню старта
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton('Рассчитать'), types.KeyboardButton('Информация'), types.KeyboardButton('Купить'), types.KeyboardButton('Регистрация'))
    await message.answer('Выберите действие:', reply_markup=keyboard)

# Функция для отображения списка продуктов
@dp.message_handler(lambda message: message.text == 'Купить')
async def get_buying_list(message: types.Message):
    products = get_all_products()

    for product in products:
        await message.answer(f'Название: {product["title"]} | Описание: {product["description"]} | Цена: {product["price"]}')
        await message.answer_photo(product["image"])

    inline_keyboard = types.InlineKeyboardMarkup()
    for product in products:
        inline_keyboard.add(types.InlineKeyboardButton(product["title"], callback_data=f'product_{product["title"]}'))

    await message.answer('Выберите продукт для покупки:', reply_markup=inline_keyboard)

# Функция для подтверждения покупки
@dp.callback_query_handler(lambda call: call.data.startswith('product_'))
async def send_confirm_message(call: types.CallbackQuery):
    product_name = call.data.split('_')[1]
    await call.message.answer(f"Вы успешно приобрели продукт: {product_name}!")
    await call.answer()

# Функция для начала регистрации
@dp.message_handler(lambda message: message.text == 'Регистрация')
async def sign_up(message: types.Message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()

# Функция для обработки имени пользователя
@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text
    if is_included(username):
        await message.answer("Пользователь существует, введите другое имя:")
    else:
        await state.update_data(username=username)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()

# Функция для обработки email
@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()

# Функция для обработки возраста и завершения регистрации
@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await message.answer("Регистрация успешно завершена!")
    await state.finish()

    # Возвращение в меню старта
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton('Рассчитать'), types.KeyboardButton('Информация'), types.KeyboardButton('Купить'), types.KeyboardButton('Регистрация'))
    await message.answer('Выберите действие:', reply_markup=keyboard)

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
