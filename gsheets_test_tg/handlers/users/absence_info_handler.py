
from aiogram.dispatcher.storage import FSMContext
from aiogram.types.reply_keyboard import ReplyKeyboardRemove
import pickle
from Get_sheets import get_sheets, get_sheets_by
from data.config import ADMINS
from keyboards.default.freshman_subjects import freshman_menu
from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from loader import dp, bot


@dp.message_handler(state="student_id")
async def get_student_id(msg: Message, state:FSMContext):
    student_id = msg.text

    if len(student_id)==7 and student_id.upper().startswith("21SE"):
            
        await state.update_data({
            "student_id": student_id
        })
        await msg.answer("Now, Please provide subject that you are lokking for", reply_markup=(freshman_menu))
        await state.set_state("subject")
    else:
        await msg.answer("<b>Please check your ID and try again!</b>")
        await state.set_state("student_id")



@dp.message_handler(state="subject")
async def get_suject(msg:Message, state:FSMContext):

    id  = await state.get_data()
    student_id = id.get("student_id")
    print(student_id)
    work_sheet = msg.text
    try:
        data = f"{work_sheet}\n"
        data += get_sheets(student_id.upper(), work_sheet)
        if data:
            await msg.answer(f"<code>{data}</code>", reply_markup=ReplyKeyboardRemove())
            await state.set_state("student_id")
        with open('token_sheets_v4.pickle', 'rb') as token:
            cred = pickle.load(token)
            print(cred)
    except Exception as e:
        print(e)
        await bot.send_message(chat_id=ADMINS[0],text=f"{e}")
        await msg.answer("I couldn't find your ID,try again ")
        await state.set_state("student_id")
