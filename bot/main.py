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
    Mahsulot_Filter_state = State()


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
async def orqaga1(call: types.CallbackQuery):
    try:
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=Katalog1)
    except:
        await call.answer('Siz oldin >> tugmasini bosing')


@dp.callback_query_handler(text='orqaga',
                           state=SHogirdchalar.Category_Filter_state)
async def orqaga2(call: types.CallbackQuery):
    try:
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=Katalog1)
    except:
        await call.answer('Siz oldin >> tugmasini bosing')






# databaseeeeeeeeeeeeeeeeeeeeeee

from sqlite3 import connect

con = connect('C:/Users/momin/PycharmProjects/OnlineShopDRF/db.sqlite3')
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
    await call.message.answer('Kategoriyalar', reply_markup=buttons)
    # await bot.send_message(call.message.chat.id, 'Kategoriyalar', reply_markup=buttons)
    await SHogirdchalar.Category_Filter_state.set()


@dp.callback_query_handler(state=SHogirdchalar.Category_Filter_state)
async def _filt_by_category(call: types.CallbackQuery, state: FSMContext):
    mahsulot_category = call.data
    filter_kategoriya = cur.execute('SELECT id FROM SalerApp_productmodel WHERE kategoriya = ?',
                                    (mahsulot_category,)).fetchone()
    id_category = filter_kategoriya[0]

    sub_category_filter = cur.execute('SELECT sub_category FROM SalerApp_categorypartmodel WHERE category_name_id = ?',
                                      (id_category,)).fetchall()
    sub_buttons = InlineKeyboardMarkup()
    for i in sub_category_filter:
        sub_buttons.add(InlineKeyboardButton(text=i[0], callback_data=i[0]))

    sub_buttons.add(InlineKeyboardButton('<<', callback_data='orqaga'))
    print(sub_category_filter)
    await call.message.answer(f'{call.data}', reply_markup=sub_buttons)
    await SHogirdchalar.Mahsulot_Filter_state.set()


@dp.callback_query_handler(state=SHogirdchalar.Mahsulot_Filter_state)
async def mahsulot_sender(call: types.CallbackQuery, state: FSMContext):
    sub_category = call.data
    mahsulotlar = cur.execute('SELECT product_name FROM SalerApp_productpartmodel WHERE last_category_id = ?',
                              (sub_category,)).fetchall()
    mahsulotlar_button = InlineKeyboardMarkup()
    for i in mahsulotlar:
        mahsulotlar_button.add(InlineKeyboardButton(text=f'{i[0]}', callback_data=i[0]))

    mahsulotlar_button.add(InlineKeyboardButton('<<', callback_data='orqaga'))
    await call.message.answer(call.data, reply_markup=mahsulotlar_button)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
