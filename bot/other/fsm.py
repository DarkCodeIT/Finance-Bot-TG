from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class ClientState(StatesGroup):
    CURR_FROM = State()
    CURR_TO = State()