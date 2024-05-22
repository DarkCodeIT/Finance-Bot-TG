from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command

from bot.keyboard import inline_kb


router = Router()

@router.message(Command(commands=["start"]))
async def start(message: Message, state: FSMContext):

    await state.clear()

    await message.answer(text=f"Привет *{message.from_user.first_name}* ^_^", reply_markup=await inline_kb.start_menu())
