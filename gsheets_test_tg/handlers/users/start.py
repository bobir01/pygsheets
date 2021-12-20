from os import stat
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Hi , {message.from_user.full_name}! send me your student \
id and I will tell you all information about your attendece of precalculus")
    await state.set_state("student_id")