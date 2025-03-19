from itertools import product

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
# from aiogram.client.default import DefaultBotProperties
from aiogram import types
import asyncio
import bcrypt
import crud_functions
from crud_functions import add_user
import hashlib, binascii

def hash_with_pbkdf2(password, salt, iterations=100000):
    password_b = password.encode("utf-8")
    salt_b = salt.encode("utf-8")
    dk = hashlib.pbkdf2_hmac('sha256', password_b, salt_b, iterations)
    return binascii.hexlify(dk).decode()

API_TOKEN = '7615066286:AAGnncLkc1IUUmKKYXaCet-QHhE9IbVN474'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

button1 = KeyboardButton(text = 'Рассчитать')
button2 = KeyboardButton(text='Купить')
button3 = KeyboardButton(text='Информация')
button4 = KeyboardButton(text='Выйти из расчёта')
button5 = KeyboardButton(text='Вход/Регистрация')
kb = ReplyKeyboardMarkup(resize_keyboard=True).row(
    button1, button2).row(
    button3, button4).row(button5)


button_in1 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
button_in2 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
button_in3 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
button_in4 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
kb_in = InlineKeyboardMarkup().row(button_in1, button_in2, button_in3, button_in4)

button_reg1 = InlineKeyboardButton(text='Регистрация', callback_data='registration')
button_reg2 = InlineKeyboardButton(text='Вход', callback_data='loging')
kb_reg = InlineKeyboardMarkup().add(button_reg1, button_reg2)

button_fill1 = InlineKeyboardButton(text='Обновить', callback_data='fill_yes')
button_fill2 = InlineKeyboardButton(text='Не надо', callback_data='fill_no')
kb_fill = InlineKeyboardMarkup().add(button_fill1, button_fill2)

button_gen1 = InlineKeyboardButton(text='Мужчина', callback_data='fill_man')
button_gen2 = InlineKeyboardButton(text='Женщина', callback_data='fill_woman')
kb_gender = InlineKeyboardMarkup().add(button_gen1, button_gen2)

products = crud_functions.get_all_products()

class UserState(StatesGroup):
    username = State()
    userpass = State()
    email = State()
    age = State()
    growth = State()
    weight = State()
    gender = State()
    calories = State()
    balance = State()

@dp.message_handler(commands=['start'])
async def main_menu(message):
    await message.answer('Выберите в меню нужное действие:', reply_markup=kb) #kb_fill)

@dp.message_handler(text='Информация')
async def get_formulas(message):
    formulas_text = ("для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5\n"
                     "для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161")
    await message.answer(formulas_text)

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    buting_text_1 = (f'Название: {products[0][1]} | Описание: {products[0][2]} | Цена: {products[0][3]}\n')
    await message.answer(buting_text_1)
    with open('files/Tab11.png', 'rb') as img1:
        await message.answer_photo(img1)
    buting_text_2 = (f'Название: {products[1][1]} | Описание: {products[1][2]} | Цена: {products[1][3]}\n')
    await message.answer(buting_text_2)
    with open('files/Tab12.png', 'rb') as img2:
        await message.answer_photo(img2)
    buting_text_3 = (f'Название: {products[2][1]} | Описание: {products[2][2]} | Цена: {products[2][3]}\n')
    await message.answer(buting_text_3)
    with open('files/Tab13.png', 'rb') as img3:
        await message.answer_photo(img3)
    buting_text_4 = (f'Название: {products[3][1]} | Описание: {products[3][2]} | Цена: {products[3][3]}\n')
    await message.answer(buting_text_4)
    with open('files/Tab14.png', 'rb') as img4:
        await message.answer_photo(img4)
    await message.answer('Выберите продукт для покупки:', reply_markup=kb_in)


@dp.message_handler(text='Вход/Регистрация')
async def sing_up (message):
    await message.answer(f'Здравствуйте, <b>{message.from_user.first_name} {message.from_user.last_name}</b> \n'
                         f'Вы вошли как пользователь: <i> {message.from_user.username}</i>', parse_mode=types.ParseMode.HTML)
    await UserState.username.set()
    res = crud_functions.is_included(message.from_user.username)
    if res[0] == '':
        await message.answer('Вас нет среди пользователей. Зарегистрируйтесь: определите пароль - ')
        await UserState.userpass.set()
    else:
        await message.answer('Введите пароль:')
        await UserState.userpass.set()


@dp.message_handler(text='Рассчитать')
async def set_age (message,state):
    calories_text = ('Введите свой возраст -')
    await message.answer(calories_text)
    await UserState.age.set()


@dp.message_handler(state=UserState.username)
async def set_username(message, state):
    await state.update_data(data_username=message.from_user.username)
    print(f'data["data_username"] - {data["data_username"]}')
    data = await state.get_data()
    res = crud_functions.is_included(data["data_username"])
    if res[0] == '':
        await message.answer('Вас нет среди пользователей. Зарегистрируйтесь: определите пароль - ')
        await UserState.userpass.set()
    else:
        await message.answer('Введите пароль:')
        await UserState.userpass.set()

@dp.message_handler(state = UserState.userpass)
async def set_userpass(message, state):
     global username, userpass
     userpass = message.text
     await state.update_data(data_userpass = message.text)
     data = await state.get_data()
     user = message.from_user.username
     username = message.from_user.username
     userpass= data["data_userpass"]
     hashed_password_pbkdf2 = hash_with_pbkdf2(userpass, username)
     res = crud_functions.is_included(message.from_user.username)
     if res[0] == '':
         crud_functions.add_user(message.from_user.username, hashed_password_pbkdf2) #data["data_userpass"])
         await message.answer('Введите Вашу элекронную почту:')
         await UserState.email.set()
     else:
         user_find = crud_functions.get_user(user)
         if user_find[1] == hashed_password_pbkdf2: #data["data_userpass"]:
             if user_find[6] == 'Мужчина':
                gender = 'мужчин'
             elif user_find[6] == 'Женщина':
                 gender = 'женщин'
             else:
                 gender = '?????'
             if user_find[3] == '' or user_find[4] == '' or user_find[5] == '' or user_find[3] == 0 or user_find[4] == 0 or user_find[5] == 0:
                 mess = 'Отсутствуют Ваши данные для расчёта. Скорректировать или заполнить данные?,'
                 await message.answer(f'Ваше имя: {user_find[0]} \n'
                                      f'Ваш пароль: {userpass} \n '
                                      f'Ваша электронная почта: {user_find[2]} \n '
                                      f'Ваш возраст: {user_find[3]} \n '
                                      f'Ваш рост: {user_find[4]} \n '
                                      f'Ваш вес: {user_find[5]} \n '
                                      f'Норма калорий для {gender} - {user_find[7]} \n')
                 username = user_find[0]
                 userpass = user_find[1]
                 await message.answer('Выберите в меню нужное действие:', reply_markup=kb_fill)  # kb_fill)
                 await state.finish()
             else:
                 await message.answer(f'Ваше имя: {user_find[0]} \n'
                                      f'Ваш пароль: {userpass} \n '
                                      f'Ваша электронная почта: {user_find[2]} \n '
                                      f'Ваш возраст: {user_find[3]} \n '
                                      f'Ваш рост: {user_find[4]} \n '
                                      f'Ваш вес: {user_find[5]} \n '
                                      f'Норма калорий для {gender} - {user_find[7]} \n')
                 username = user_find[0]
                 userpass = user_find[1]
                 await message.answer('Выберите в меню нужное действие:', reply_markup=kb)  # kb_fill)
                 await state.finish()
         else:
            await message.answer(f'Вы ввели неправильный пароль. Повторите ввод пароля или запустите бот заново /start')
            await sing_up_1 (message)

@dp.callback_query_handler(text='fill_yes')
async def filling_again (message):
    await message.message.answer('Введите Вашу элекронную почту:')
    await UserState.email.set()

@dp.callback_query_handler(text='fill_no')
async def filling_no (message):
    await UserState.email.set()
    await message.message.answer('Выберите в меню нужное действие: 4', reply_markup=kb)
    await main_menu(message)


@dp.callback_query_handler(text='loging')
async def sing_up_1 (message):
    await UserState.username.set()



@dp.message_handler(state = UserState.email)
async def set_email(message, state):
     await state.update_data(data_email = message.text)
     await state.update_data(data_username = username)
     await state.update_data(data_userpass  = userpass)
     data = await state.get_data()
     global email
     email = data["data_email"]
     await message.answer(f'Ваше имя: {data["data_username"]} \n'
                          f'Ваш пароль: {data["data_userpass"]} \n '
                          f'Ваша электронная почта: {data["data_email"]} \n '
                          f'                                 Введите свой возраст -')
     await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_age(message, state):
     global age
     await state.update_data(data_age = message.text)
     await state.update_data(data_username='Неопределён')
     await state.update_data(data_userpass='Неопределён')
     await state.update_data(data_email='Неопределена')

     data = await state.get_data()
     await message.answer(f'Ваше имя: {data["data_username"]} \n'
                          f'Ваш пароль: {data["data_userpass"]} \n '
                          f'Ваша электронная почта: {data["data_email"]} \n '
                          f'Ваш возраст: {data["data_age"]} \n '
                          f'                                 Введите свой рост -')
     age = data["data_age"]
     await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
     global growth
     await state.update_data(data_growth = message.text)
     data = await state.get_data()
     growth = data["data_growth"]
     await message.answer(f'Ваше имя: {data["data_username"]} \n'
                          f'Ваш пароль: {data["data_userpass"]} \n '
                          f'Ваша электронная почта: {data["data_email"]} \n '
                          f'Ваш возраст: {data["data_age"]} \n '
                          f'Ваш рост: {data["data_growth"]} \n '
                          f'                                 Введите свой вес -')
     await UserState.weight.set()

@dp.message_handler(state = UserState.weight)#, text='Ошибка при выборе принадлежности к полу')
async def set_gender(message, state):
     global weight
     await state.update_data(data_weight = message.text)
     global username, userpass, email, age, growth, weight

     data = await state.get_data()
     username = data["data_username"]
     userpass = data["data_userpass"]
     email = data["data_email"]
     age = data["data_age"]
     growth = data["data_growth"]
     weight = data["data_weight"]
     await message.answer(f'Ваше имя: {username} \n'
                          f'Ваш пароль: {userpass} \n '
                          f'Ваша электронная почта: {email} \n '
                          f'Ваш возраст: {age} \n '
                          f'Ваш рост: {growth} \n '
                          f'Ваш вес: {weight} \n '
                          f'                  Введите принадлежность к полу (Мужчина / Женщина):', reply_markup=kb_gender)
     await state.finish()

@dp.callback_query_handler(text=["fill_man", "fill_woman"])
async def send_calories(call: types.CallbackQuery):
     if call.data == 'fill_man' or call.data == 'fill_woman':
         man_calories = 10 * int(weight) + 6.25 * int(growth) + 5 * int(age) + 5
         woman_calories = 10 * int(weight) + 6.25 * int(growth) + 5 * int(age) - 161
         if call.data == ('fill_man'):
             await call.message.answer(f'Ваше имя: {username} \n'
                                  f'Ваш пароль: {userpass} \n '
                                  f'Ваша электронная почта: {email} \n '
                                  f'Ваш возраст: {age} \n '
                                  f'Ваш рост: {growth} \n '
                                  f'Ваш вес: {weight} \n '
                                  f'                     Норма калорий для мужчин - {int(man_calories)} \n')
             gender = "Мужчина"
             calories = int(man_calories)
             balance = 1000
             if username == 'Неопределён':
                 call.message.text = '/start'
             else:
                 crud_functions.update_user(username, hash_with_pbkdf2(userpass, username), email, age, growth, weight, gender, calories, balance)
         elif call.data == 'fill_woman':
             await call.message.answer(f'Ваше имя: {username} \n'
                                  f'Ваш пароль: {userpass} \n '
                                  f'Ваша электронная почта: {email} \n '
                                  f'Ваш возраст: {age} \n '
                                  f'Ваш рост: {growth} \n '
                                  f'Ваш вес: {weight} \n '
                                  f'                      Норма калорий для женщин - {int(woman_calories)}')
             gender = "Женщина"
             calories = int(woman_calories)
             balance = 1000
             crud_functions.update_user(username, hash_with_pbkdf2(userpass, username), email, age, growth, weight, gender, calories, balance)
         else:
             await call.answer(f'Ошибка при выборе принадлежности к полу')
     else:
         call.text = '/start'
         await main_menu(call.message)
     call.text = '/start'
     await main_menu(call.message)

@dp.message_handler(state = UserState.gender)
async def set_gender_mist(message, state):
     data = await state.get_data()
     await message.answer(f'Ваше имя: {data["data_username"]} \n'
                          f'Ваш пароль: {data["data_userpass"]} \n '
                          f'Ваша электронная почта: {data["data_email"]} \n '
                          f'Ваш возраст: {data["data_age"]} \n '
                          f'Ваш рост: {data["data_age"]} \n '
                          f'Ваш вес: {data["data_weight"]} \n '
                          f'                                 Введите принадлежность к полу (М / Ж): -')
     await UserState.gender.set()

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(message):
    confirm_text = ("Вы успешно приобрели продукт!")
    await message.answer(confirm_text)



@dp.message_handler(text=['Выйти из расчёта'])
async def exit(message):
    await message.answer('Выход', reply_markup=ReplyKeyboardRemove())

@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение')



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


