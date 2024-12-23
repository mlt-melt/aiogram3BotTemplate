from aiogram.utils.deep_linking import create_start_link, decode_payload
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram import types, F

from handlers.markups import *
from storage.config import dp, bot
from storage.states import tryFinish, State
from db import User


@dp.callback_query(F.data == "profile")
async def profileCall(call: types.CallbackQuery, state: FSMContext):
    await tryFinish(state)
    link = await create_start_link(bot, str(call.from_user.id))
    await call.message.edit_text(f'Здравствуйте, {call.from_user.first_name}\n\nВаша реферальная ссылка:\n<code>{link}</code>', reply_markup=profile_mpk())