import logging
from aiogram import executor
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

API_TOKEN = '6643960998:AAFNK97Rx7OsvLA7WDUYcxII4mBUnUs6dfc'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())
from keyboards.default import asosiy_menyu
from keyboards.inline import Katalog1, Katalog2


@dp.message_handler(commands='start')
async def starter(message: types.Message):
    await message.answer(f"Assalomu ALeykum <code>{message.from_user.full_name}</code>", reply_markup=asosiy_menyu)


@dp.message_handler(text='Katalog')
async def katalogcha(message: types.Message):
    await message.answer('Kataloglar', reply_markup=Katalog1)


@dp.callback_query_handler(text='oldinga')
async def katalogcha(call: types.CallbackQuery):
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=Katalog2)


@dp.callback_query_handler(text='orqaga')
async def katalogcha2(call: types.CallbackQuery):
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=Katalog1)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
