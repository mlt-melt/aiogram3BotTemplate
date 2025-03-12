from aiogram import types

# def example_mkp():
#     btns = [
#         [
#             types.InlineKeyboardButton(text="Ряд 1, Кнопка 1", callback_data="callback_1_1"),
#             types.InlineKeyboardButton(text='Ряд 1, Кнопка 2', callback_data="callback_1_2")
#         ],
#         [
#             types.InlineKeyboardButton(text="Ряд 2, Кнопка 1", callback_data="callback_2_1"),
#             types.InlineKeyboardButton(text='Ряд 2, Кнопка 2', callback_data="callback_2_2")
#         ],
#     ]
#     return types.InlineKeyboardMarkup(inline_keyboard=btns)

def start_mkp():
    btns = [
        [
            types.InlineKeyboardButton(text="Профиль", callback_data="profile")
        ],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=btns)

def to_menu_mpk():
    btns = [
        [
            types.InlineKeyboardButton(text="Вернуться в меню", callback_data="start")
        ],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=btns)

def cancel_mpk():
    btns = [
        [types.InlineKeyboardButton(text="Отменить", callback_data="start")],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=btns)

def profile_mpk():
    btns = [
        [
            types.InlineKeyboardButton(text="Связаться с разработчиками", callback_data="contact_with_devs")
        ],
        [
            types.InlineKeyboardButton(text="Вернуться в меню", callback_data="start")
        ],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=btns)