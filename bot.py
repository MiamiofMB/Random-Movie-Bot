from random import *
from aiogram import *
from parser import rand_mov
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


token = '6148500514:AAFeSnw9pIu-mm2C2yuLJl2_nTdSVn0vRew'
bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def begin(message: types.Message):
    await bot.send_message(message.chat.id,'Привет! Введи жанр фильма  который ты хочешь посмотерть!')
@dp.message_handler(text=['комедия','драма','триллер','аниме','биография','боевик','Комедия','Драма','Триллер','Аниме','Биография','Боевик','Детектив' ,'детектив','Вестерн','вестерн'])
async def help(message: types.Message):

    if message.text == 'комедия' or message.text == 'Комедия':
        mov = randint(1, 10)
        ans = text = rand_mov('комедия')['docs'][mov]
        await message.answer(text=ans['name'])
        await message.answer(text=ans['description'])
        await message.answer(text=ans['poster']['url'])
    elif message.text == 'драма' or message.text == 'Драма':
        mov = randint(1, 10)
        ans = text = rand_mov('драма')['docs'][mov]
        await message.answer(text=ans['name'])
        await message.answer(text=ans['description'])
        await message.answer(text=ans['poster']['url'])
    elif message.text == 'триллер' or message.text == 'Триллер':
        mov = randint(1, 10)
        ans = text = rand_mov('триллер')['docs'][mov]
        await message.answer(text=ans['name'])
        await message.answer(text=ans['description'])
        await message.answer(text=ans['poster']['url'])
    elif message.text == 'аниме' or message.text == 'Аниме':
        mov = randint(1, 10)
        ans = text = rand_mov('аниме')['docs'][mov]
        await message.answer(text=ans['name'])
        await message.answer(text=ans['description'])
        await message.answer(text=ans['poster']['url'])
    elif message.text == 'биография' or message.text == 'Биография':
        mov = randint(1, 10)
        ans = text=rand_mov('биография')['docs'][mov]
        await message.answer(text=ans['name'])
        await message.answer(text=ans['description'])
        await message.answer(text=ans['poster']['url'])
    elif message.text == 'боевик' or message.text == 'Боевик':
        mov = randint(1, 10)
        ans = text = rand_mov('боевик')['docs'][mov]
        await message.answer(text=ans['name'])
        await message.answer(text=ans['description'])
        await message.answer(text=ans['poster']['url'])
    elif message.text == 'вестерн' or message.text == 'Вестерн':
        mov = randint(1, 10)
        ans = text = rand_mov('вестерн')['docs'][mov]
        await message.answer(text=ans['name'])
        await message.answer(text=ans['description'])
        await message.answer(text=ans['poster']['url'])
    elif message.text == 'детектив' or message.text == 'Детектив':
        mov = randint(1, 10)
        ans = text = rand_mov('детектив')['docs'][mov]
        await message.answer(text=ans['name'])
        await message.answer(text=ans['description'])
        await message.answer(text=ans['poster']['url'])
    else:
        await message.answer(text='Жанр не найден, пиши грамотнее,дубина')

executor.start_polling(dp)
