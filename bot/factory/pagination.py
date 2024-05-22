from aiogram.filters.callback_data import CallbackData


class Menu(CallbackData, prefix="menu"):
    action: str


class FromTo(CallbackData, prefix="from_to"):
    action: str


class CurrFrom(CallbackData, prefix="curr_from"):
    action: str
    page: int


class CurrTo(CallbackData, prefix="curr_to"):
    action: str
    page: int


class Back(CallbackData, prefix="back"):
    action: str
    page: int = -1


class Next(CallbackData, prefix="next"):
    action: str
    page: int = -1