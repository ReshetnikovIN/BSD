from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio



API_TOKEN = ''
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

button1 = KeyboardButton(text = 'Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Выйти из расчёта')
kb = ReplyKeyboardMarkup().row(
    button1, button2, button3)

kb_in = InlineKeyboardMarkup()
button_in1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_in2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_in.add(button_in1)
kb_in.add(button_in2)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb_in)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    formulas_text = ("для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5\n"
                     "для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161")
    await call.answer(formulas_text)


@dp.callback_query_handler(text='calories')
async def set_age (call):
    calories_text = ('Введите свой возраст -')
    await call.answer(calories_text)
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
     await state.update_data(data_age = message.text)
     data = await state.get_data()
     await message.answer(f'Ваш возраст: {data["data_age"]} \n '
                          f'                                 Введите свой рост -')
     await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
     await state.update_data(data_growth = message.text)
     data = await state.get_data()
     await message.answer(f'Ваш возраст: {data["data_age"]} \n '
                          f'Ваш рост: {data["data_growth"]} \n '
                          f'                                 Введите свой вес -')
     await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
     await state.update_data(data_weight = message.text)
     data = await state.get_data()
     man_calories = 10 * int(data["data_weight"]) + 6.25 * int(data["data_growth"]) + 5 * int(data["data_age"]) + 5
     woman_calories = 10 * int(data["data_weight"]) + 6.25 * int(data["data_growth"]) + 5 * int(data["data_age"]) - 161
     await message.answer(f'Для возраста: {data["data_age"]} \n '
                          f'                вecа: {data["data_growth"]} \n '
                          f'              роста: {data["data_weight"]} \n '
                          f'                     Норма калорий для мужчин - {int(man_calories)} \n'
                          f'                      Норма калорий для женщин - {int(woman_calories)}')
     await state.finish()

@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение')



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


