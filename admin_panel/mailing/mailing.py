from aiogram.fsm.context import FSMContext
from aiogram import types, F

from storage.config import dp, bot
from db import User

from .markups import *
from .states import tryFinish, MailingAll, MailingUser

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

@dp.callback_query(F.data == "admin_mailing_user")
async def mailingUserCall(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(f'Сообщение конретному юзеру. Введите id юзера', reply_markup=mailing_cancel_mpk())
    await state.set_state(MailingUser.Id)

@dp.message(MailingUser.Id)
async def mailingUserIdCall(message: types.Message, state: FSMContext):
    tg_id = message.text
    await state.update_data(tg_id=tg_id)
    await message.answer(f'Юзер {tg_id}\n\nВведите текст:', reply_markup=mailing_cancel_mpk())
    await state.set_state(MailingUser.Msg)

@dp.message(MailingUser.Msg)
async def mailingUserGoCall(message: types.Message, state: FSMContext):
    user_id = (await state.get_data())["tg_id"]
    try:
        await bot.copy_message(user_id, message.from_user.id, message.message_id)
        await message.answer(f'Сообщение отправлено', reply_markup=mailing_after_mpk())
    except Exception as ex:
        await message.answer(f'Сообщение не отправлено. Ошибка - {traceback.format_exc()}', reply_markup=mailing_after_mpk())
    await tryFinish(state)