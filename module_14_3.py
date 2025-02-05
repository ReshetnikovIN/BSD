from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio



API_TOKEN = ''
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

button1 = KeyboardButton(text = 'Рассчитать')
button2 = KeyboardButton(text='Купить')
button3 = KeyboardButton(text='Информация')
button4 = KeyboardButton(text='Выйти из расчёта')
kb = ReplyKeyboardMarkup().row(
    button1, button2).row(
    button3, button4)

button_in1 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
button_in2 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
button_in3 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
button_in4 = InlineKeyboardButton(text='Product4', callback_data='product_buying')

kb_in = InlineKeyboardMarkup().row(button_in1, button_in2, button_in3, button_in4)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb)

@dp.message_handler(text='Информация')
async def get_formulas(message):
    formulas_text = ("для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5\n"
                     "для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161")
    await message.answer(formulas_text)


@dp.message_handler(text='Рассчитать')
async def set_age (message):
    calories_text = ('Введите свой возраст -')
    await message.answer(calories_text)
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

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    buting_text_1 = (f'Название: Product1 | Описание: описание 1 | Цена: {1 * 100}\n')
    await message.answer(buting_text_1)
    with open('files/Tab11.png', 'rb') as img1:
        await message.answer_photo(img1)
    buting_text_2 = (f'Название: Product2 | Описание: описание 2 | Цена: {2 * 100}\n')
    await message.answer(buting_text_2)
    with open('files/Tab12.png', 'rb') as img2:
        await message.answer_photo(img2)
    buting_text_3 = (f'Название: Product3 | Описание: описание 3 | Цена: {3 * 100}\n')
    await message.answer(buting_text_3)
    with open('files/Tab13.png', 'rb') as img3:
        await message.answer_photo(img3)
    buting_text_4 = (f'Название: Product4 | Описание: описание 4 | Цена: {4 * 100}\n')
    await message.answer(buting_text_4)
    with open('files/Tab14.png', 'rb') as img4:
        await message.answer_photo(img4)
    await message.answer('Выберите продукт для покупки:', reply_markup=kb_in)
        # f'Название: Product2 | Описание: описание 2 | Цена: {2 * 100}\n'
        #            f'Название: Product3 | Описание: описание 3 | Цена: {3 * 100}\n'
        #            f'Название: Product4 | Описание: описание 4 | Цена: {4 * 100}\n'
        #            )
    # await message.answer(buting_text, reply_markup=kb_in)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    confirm_text = ("Вы успешно приобрели продукт!")
    await call.answer(confirm_text)



@dp.message_handler(text=['Выйти из расчёта'])
async def exit(message):
    await message.answer('Выход', reply_markup=ReplyKeyboardRemove())


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение')



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


