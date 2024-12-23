from aiogram.fsm.context import FSMContext
from aiogram import types, F

from storage.config import dp, bot
from db import User

from .markups import *
from .states import tryFinish, MailingAll

@dp.callback_query(F.data == "admin_mailing")
async def mailingCall(call: types.CallbackQuery, state: FSMContext):
    await tryFinish(state)
    await call.message.edit_text(f'Раздел рассылок. Кого вы хотите уведомить?', reply_markup=mailing_mpk())

@dp.callback_query(F.data == "admin_mailing_all")
async def mailingAllCall(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(f'Рассылка по всем юзерам. Введите сообщение', reply_markup=mailing_cancel_mpk())
    await state.set_state(MailingAll.Msg)

@dp.message(MailingAll.Msg)
async def mailingAllGoCall(message: types.Message, state: FSMContext):
    users = User.all()
    await message.answer(f'Рассылка началась')
    for i in users:
        i: User
        try:
            await bot.copy_message(i.tg_id, message.from_user.id, message.message_id)
        except:
            pass
    await message.answer(f'Рассылка завершена', reply_markup=mailing_after_mpk())
    await tryFinish(state)