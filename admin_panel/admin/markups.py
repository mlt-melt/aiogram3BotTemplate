from aiogram import types

def admin_mpk():
    btns = [
        [types.InlineKeyboardButton(text="Рассылка", callback_data=f'admin_mailing')],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=btns)

def back_to_admin_panel_mpk():
    btns = [
        [types.InlineKeyboardButton(text="Вернуться в админ-панель", callback_data=f'admin')],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=btns)