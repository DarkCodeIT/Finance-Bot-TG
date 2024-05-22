from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from ..factory.pagination import Menu, FromTo, Back, Next, CurrFrom, CurrTo
from tool_data.all_data import currencys


async def start_menu():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Меню", callback_data=Menu(action="get_menu").pack())
    )

    return builder.as_markup()


async def main_menu():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Новости📰", callback_data=Menu(action="news").pack()),
        InlineKeyboardButton(text="Курсы валют💵", callback_data=Menu(action="curr").pack()),
        InlineKeyboardButton(text="Курсы крипты💰", callback_data=Menu(action="curr_crypt").pack()),
        InlineKeyboardButton(text="О насℹ️", callback_data=Menu(action="about_us").pack())
    )

    builder.adjust(1, 2, 1)
    return builder.as_markup()


# Создание клавиатур для курса валют
async def curr_from_to():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="From💶", callback_data=FromTo(action="from").pack()),
        InlineKeyboardButton(text='To💷', callback_data=FromTo(action="to").pack()),
        InlineKeyboardButton(text='⬅️Back', callback_data=Back(action="back_to_menu").pack())
    )

    builder.adjust(2, 1)
    return builder.as_markup()


async def curr_from(page: int):
    builder = InlineKeyboardBuilder()
    buttons = []

    if page == 1:
        for index in range(len(currencys)):
            if index == 10:
                break

            buttons.append(InlineKeyboardButton(text=currencys[index],
                                                callback_data=CurrFrom(action=currencys[index], page=1).pack()))

        buttons.append(InlineKeyboardButton(text="⬅Back", callback_data=Back(action="go_from_to").pack()))
        buttons.append(InlineKeyboardButton(text="Next➡", callback_data=Next(action="next_curr_from", page=1).pack()))

        builder.row(*buttons)
        builder.adjust(2)

        return builder.as_markup()

    elif page == 2:
        for index in range(10, len(currencys)):
            buttons.append(InlineKeyboardButton(text=currencys[index],
                                                callback_data=CurrFrom(action=currencys[index], page=2).pack()))

        buttons.append(InlineKeyboardButton(text="⬅Back", callback_data=Back(action="go_curr_from_page", page=2).pack()))

        builder.row(*buttons)
        builder.adjust(2)

        return builder.as_markup()


async def curr_to(page: int):
    builder = InlineKeyboardBuilder()
    buttons = []

    if page == 1:
        for index in range(len(currencys)):
            if index == 10:
                break

            buttons.append(InlineKeyboardButton(text=currencys[index],
                                                callback_data=CurrTo(action=currencys[index], page=1).pack()))

        buttons.append(InlineKeyboardButton(text="⬅Back", callback_data=Back(action="go_from_to").pack()))
        buttons.append(InlineKeyboardButton(text="Next➡", callback_data=Next(action="next_curr_to", page=1).pack()))

        builder.row(*buttons)
        builder.adjust(2)

        return builder.as_markup()

    elif page == 2:
        for index in range(10, len(currencys)):
            buttons.append(InlineKeyboardButton(text=currencys[index],
                                                callback_data=CurrTo(action=currencys[index], page=2).pack()))

        buttons.append(InlineKeyboardButton(text="⬅Back", callback_data=Back(action="go_curr_to_page", page=2).pack()))

        builder.row(*buttons)
        builder.adjust(2)

        return builder.as_markup()


async def back_btn():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="⬅Back", callback_data=Back(action="back_to_FromTo").pack())
    )
    return builder.as_markup()
