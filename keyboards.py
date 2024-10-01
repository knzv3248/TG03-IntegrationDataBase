from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main_button = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Привет"), KeyboardButton(text="Пока")]
], resize_keyboard=True)

inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Новости", url='https://dzen.ru/')],
   [InlineKeyboardButton(text="Музыка", url='https://music.yandex.ru/home?a')],
   [InlineKeyboardButton(text="Видео", url='https://yandex.ru/video/search?from_block=efir_newtab&stream_channel=35&text=%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE&feed=1')]
])

list_buttons = ["Опция 1", "Опция 2"]
async def test_keyboard():
   keyboard = InlineKeyboardBuilder()
   for key in list_buttons:
       keyboard.add(InlineKeyboardButton(text=key, url='https://dzen.ru/'))
   return keyboard.adjust(2).as_markup()
   # keyboard = InlineKeyboardMarkup(row_width=2)
   # for key in list_buttons:
   #    # Используем callback_data для обработки нажатия на кнопку
   #    keyboard.add(InlineKeyboardButton(text=key, callback_data=key))
   # return keyboard

expansion_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Показать больше", callback_data='show_more')],
])
