import logging
from aiogram import executor
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.dispatcher.filters import Text
API_TOKEN = '5118382129:AAG66mR8-G-wqEisPlkIpyDzkAUPgoWAoQo'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())
from keyboards.default import asosiy_menyu
from keyboards.inline import Katalog1, Katalog2


class SHogirdchalar(StatesGroup):
    Katalog_Filter_state = State()
    Category_Filter_state = State()
    SubCategory_Filter_state = State()


@dp.message_handler(commands='start')
async def starter(message: types.Message):
    await message.answer(f"Assalomu ALeykum <code>{message.from_user.full_name}</code>", reply_markup=asosiy_menyu)


@dp.message_handler(text='Katalog')
async def katalogcha(message: types.Message):
    await message.answer('Kataloglar', reply_markup=Katalog1)
    await SHogirdchalar.Katalog_Filter_state.set()


@dp.callback_query_handler(text='oldinga',
                           state=SHogirdchalar.Katalog_Filter_state)
async def oldinga(call: types.CallbackQuery):
    try:
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=Katalog2)
    except:
        await call.answer('Siz oldin << tugmasini bosing')


@dp.callback_query_handler(text='orqaga',
                           state=SHogirdchalar.Katalog_Filter_state)
async def orqaga(call: types.CallbackQuery):
    try:
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=Katalog1)
    except:
        await call.answer('Siz oldin >> tugmasini bosing')

@dp.callback_query_handler(text='orqaga',
                           state=SHogirdchalar.Category_Filter_state)
async def orqaga(call: types.CallbackQuery):
    try:
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=Katalog1)
    except:
        await call.answer('Siz oldin >> tugmasini bosing')
# databaseeeeeeeeeeeeeeeeeeeeeee

from sqlite3 import connect

con = connect('db.sqlite3')
cur = con.cursor()


@dp.callback_query_handler(state=SHogirdchalar.Katalog_Filter_state)
async def _filt_by_katalog(call: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query_id=call.id)
    tanlov_katalog = call.data
    buttons = InlineKeyboardMarkup()
    a = cur.execute('SELECT * FROM SalerApp_productmodel WHERE katalog = ?', (str(tanlov_katalog),)).fetchall()
    for i in a:
        buttons.add(InlineKeyboardButton(i[2], callback_data=i[2]))

    buttons.add(InlineKeyboardButton('<<', callback_data='orqaga'))
    await call.message.delete()
    await bot.send_message(call.message.chat.id, 'Kategoriyalar', reply_markup=buttons)
    await SHogirdchalar.Category_Filter_state.set()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
