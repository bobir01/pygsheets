from aiogram.dispatcher.storage import FSMContext

from Get_sheets import get_sheets

from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from loader import dp

@dp.message_handler(state="student_id")
async def get_student_id(msg: Message, state:FSMContext):
    student_id = msg.text
    if len(student_id)==7 :

        data = get_sheets(student_id.upper())
        await msg.answer(data)
    

