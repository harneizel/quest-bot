from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
#главное меню
main_kb = [
    [KeyboardButton(text='🌲 Информация'),
     KeyboardButton(text='🧭 Маршруты')],
    [KeyboardButton(text='👤 Профиль'),
     KeyboardButton(text='💵 Оплата')]
]
main = ReplyKeyboardMarkup(keyboard=main_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт ниже')

#главное меню админ
main_admin_kb = [
    [KeyboardButton(text='🌲 Информация'),
     KeyboardButton(text='🧭 Маршруты')],
    [KeyboardButton(text='👤 Профиль'),
     KeyboardButton(text='💵 Оплата')],
    [KeyboardButton(text='💻 Админ панель')]
]
main_admin = ReplyKeyboardMarkup(keyboard=main_admin_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт ниже')

#панелька админа
admin_panel = [
    [KeyboardButton(text='Создать маршрут'),
     KeyboardButton(text='Показать все маршруты')],
    [KeyboardButton(text='Удалить маршрут'),
     KeyboardButton(text='🔙 Вернуться в меню')]
]
panel = ReplyKeyboardMarkup(keyboard=admin_panel,
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт ниже')

#админ выбор типа маршрута
choose_type = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='С описанием', callback_data='caption')],
    [InlineKeyboardButton(text='С собиранием геоточек', callback_data='live')],

])

#при прохождении маршрута
locate_kb = [
    [KeyboardButton(text='🔙 Вернуться в меню')],
    [KeyboardButton(text='🎯 Сбросить прогресс')]
]

locate = ReplyKeyboardMarkup(keyboard=locate_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт ниже')



#inline выбор типа маршрута
menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='С описанием', callback_data='rout_offline')],
    [InlineKeyboardButton(text='Со сбором геоточек', callback_data='rout_online')],

])

#inline проверка локации
check_loc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='📍 Проверить мою геопозицию', callback_data='send_location')],
])

progress = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='✅ Да', callback_data='yes'),
    InlineKeyboardButton(text='❌ Нет', callback_data='no')],
])

delete_route = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='С описанием', callback_data='offline'),
    InlineKeyboardButton(text='С геоточками', callback_data='online')],
])

