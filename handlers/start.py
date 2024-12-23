from aiogram.utils.deep_linking import decode_payload
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.utils.chat_action import ChatActionSender
from aiogram import types, F

from handlers.markups import *
import utils.custom_logger as cl
from utils.scripts import get_refer_id
from storage.config import dp, bot
from storage.states import tryFinish, State
from db import User


@dp.message(CommandStart())
async def startcmd(message: types.Message, command: CommandObject):
    async with ChatActionSender.typing(bot=bot, chat_id=message.from_user.id):
        referal_inviter_tg_id = get_refer_id(command.args)
        cl.log("Start Handler", "info", f"Registation (ref - {referal_inviter_tg_id})", message.from_user.id)
        fullname = f"{message.from_user.first_name}{' ' + message.from_user.last_name if message.from_user.last_name else ''}"
        User.get_or_create(message.from_user.id, fullname=fullname, username=message.from_user.username,
                        inviter_id=referal_inviter_tg_id if referal_inviter_tg_id else 0)
    await message.answer('Меню', reply_markup=start_mkp())

# @dp.callback_query(F.data == "start", State.State)
@dp.callback_query(F.data == "start")
async def startCall(call: types.CallbackQuery, state: FSMContext):
    await tryFinish(state)
    await call.message.edit_text('Меню', reply_markup=start_mkp())