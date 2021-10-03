from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# кнопки
get_link_button = InlineKeyboardButton(text='Получите ссылку!', callback_data='get_link_button')

# панель
link_panel = InlineKeyboardMarkup().add(get_link_button)
