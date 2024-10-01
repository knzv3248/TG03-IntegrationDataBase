import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery

from config import *
import keyboards as kb


bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
   await message.answer(f'Приветики, {message.from_user.first_name}', reply_markup=kb.main_button)

@dp.message(F.text == "Привет")
async def hi_button(message: Message):
   await message.answer(f'Привет, {message.from_user.first_name}!')
   # await message.answer(f'Привет, {message.from_user.first_name}!', reply_markup=kb.main_button)

@dp.message(F.text == "Пока")
async def bye_button(message: Message):
   await message.answer(f'До свидания, {message.from_user.first_name}!')


@dp.message(Command('links'))
async def my_links(message: Message):
   await message.answer('Сделайте выбор', reply_markup=kb.inline_keyboard_test)


@dp.message(Command('dynamic'))
async def dynamic(message: Message):
   await message.answer('Демонстрация расширения функционала', reply_markup=kb.expansion_inline_keyboard)

@dp.callback_query(F.data == 'Показать больше')
async def expansion(callback: CallbackQuery):
   await callback.message.edit_text('Вот свежие новости!', reply_markup=await kb.test_keyboard())

@dp.callback_query(F.data == 'show_more')
async def expansion(callback: CallbackQuery):
       await callback.message.edit_text('Выберите опцию', reply_markup=await kb.test_keyboard())

# @dp.callback_query_handler(lambda c: c.data in list_buttons)
# async def process_callback_button(callback_query: types.CallbackQuery):
#     # Отправляем сообщение с текстом нажатой кнопки
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, f"Вы выбрали: {callback_query.data}")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())