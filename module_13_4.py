from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio



API_TOKEN = ''
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text='Calories')
async def set_age(message):
    await message.answer('Введите свой возраст -')
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
     # man_calories = data["data_weight"]
     # woman_calories = 11 * float(data["data_weight"])
     await message.answer(f'Для возраста: {data["data_age"]} \n '
                          f'                вecа: {data["data_growth"]} \n '
                          f'              роста: {data["data_weight"]} \n '
                          f'                     Норма калорий для мужчин - {int(man_calories)} \n'
                          f'                      Норма калорий для женщин - {int(woman_calories)}')
     await state.finish()



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


