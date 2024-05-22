from aiogram import Router
from aiogram.types.callback_query import CallbackQuery
from aiogram.exceptions import TelegramBadRequest
from contextlib import suppress

from bot.factory.pagination import Menu, FromTo, Back, CurrFrom, CurrTo, Next
from bot.keyboard import inline_kb
from tool_data.all_data import currencys
from parser.currency_onda import get_cur
from ..other.fsm import *

router = Router()


@router.callback_query(Menu.filter())
async def main_menu_handler(call: CallbackQuery, callback_data: Menu):

    if callback_data.action == "get_menu":
        await call.message.edit_text(text="Добро пожаловать в меню помощника!\nЗдесь вы можете выбрать необходимые действия.",
                                     reply_markup=await inline_kb.main_menu())

    elif callback_data.action == "news":
        pass

    elif callback_data.action == "curr":
        await call.message.edit_text(text="Выберите валюты 'From'->'To'.", reply_markup=await inline_kb.curr_from_to())

    elif callback_data.action == "curr_crypto":
        pass

    elif callback_data.action == "about_us":
        pass


@router.callback_query(FromTo.filter())
async def from_to_handler(call: CallbackQuery, callback_data: FromTo):

    if callback_data.action == "from":
        await call.message.edit_text(text="Выберите желаемую валюту:", reply_markup=await inline_kb.curr_from(page=1))

    elif callback_data.action == "to":
        await call.message.edit_text(text="Выберите желаемую валюту:", reply_markup=await inline_kb.curr_to(page=1))


@router.callback_query(CurrFrom.filter())
async def curr_from_handler(call: CallbackQuery, callback_data: CurrFrom, state: FSMContext):

    await state.update_data(CURR_FROM=callback_data.action)
    await call.answer(text="Selected")
    data = await state.get_data()

    if "CURR_FROM" in data and "CURR_TO" in data:
        text = await get_cur(from_=data['CURR_FROM'], to_=data['CURR_TO'])
        await call.message.edit_text(text=text, reply_markup=await inline_kb.back_btn())
        await state.clear()

    else:
        await call.message.edit_text(text="Выберите валюты 'From'->'To'.", reply_markup=await inline_kb.curr_from_to())


@router.callback_query(CurrTo.filter())
async def curr_to_handler(call: CallbackQuery, callback_data: Next, state: FSMContext):

    await state.update_data(CURR_TO=callback_data.action)
    await call.answer(text="Selected")
    data = await state.get_data()

    if "CURR_FROM" in data and "CURR_TO" in data:
        text = await get_cur(from_=data['CURR_FROM'], to_=data['CURR_TO'])
        await call.message.edit_text(text=text, reply_markup=await inline_kb.back_btn())
        await state.clear()

    else:
        await call.message.edit_text(text="Выберите валюты 'From'->'To'.", reply_markup=await inline_kb.curr_from_to())


@router.callback_query(Back.filter())
async def back_handler(call: CallbackQuery, callback_data: Back, state: FSMContext):

    if callback_data.action == "back_to_menu":
        await call.message.edit_text(
            text="Добро пожаловать в меню помощника!\nЗдесь вы можете выбрать необходимые действия.",
            reply_markup=await inline_kb.main_menu())

        await state.clear()

    elif callback_data.action == "go_from_to":
        await call.message.edit_text(text="Выберите валюты 'From'->'To'.", reply_markup=await inline_kb.curr_from_to())

    elif callback_data.action == "go_curr_from_page":
        if callback_data.page == 2:
            await call.message.edit_text(text="Выберите желаемую валюту:", reply_markup=await inline_kb.curr_from(page=1))

    elif callback_data.action == "go_curr_to_page":
        if callback_data.page == 2:
            await call.message.edit_text(text="Выберите желаемую валюту:", reply_markup=await inline_kb.curr_to(page=1))

    elif callback_data.action == "back_to_FromTo":
        await call.message.edit_text(text="Выберите валюты 'From'->'To'.", reply_markup=await inline_kb.curr_from_to())
        await state.clear()


@router.callback_query(Next.filter())
async def next_handler(call: CallbackQuery, callback_data: Next):

    if callback_data.action == "next_curr_from":

        if callback_data.page == 1:
            await call.message.edit_text(text="Выберите желаемую валюту:", reply_markup=await inline_kb.curr_from(page=2))

    elif callback_data.action == "next_curr_to":

        if callback_data.page == 1:
            await call.message.edit_text(text="Выберите желаемую валюту:", reply_markup=await inline_kb.curr_to(page=2))

