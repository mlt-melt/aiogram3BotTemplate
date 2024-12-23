from aiogram.fsm.state import StatesGroup, State

async def tryFinish(state):
    try:
        await state.clear()
    except:
        pass

class MailingAll(StatesGroup):
    Msg = State()