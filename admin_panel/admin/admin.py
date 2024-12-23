from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

from storage.config import dp, admins
from db import User

from .markups import *
from .states import tryFinish


@dp.message(Command('admin'))
async def adminCmd(message: types.Message, state: FSMContext):
    if message.from_user.id in admins:
        await tryFinish(state)
        await message.answer("Админ-панель", reply_markup=admin_mpk())

@dp.callback_query(F.data == "admin")
async def adminCall(call: types.CallbackQuery, state: FSMContext):
    await tryFinish(state)
    await call.message.edit_text("Админ-панель", reply_markup=admin_mpk())