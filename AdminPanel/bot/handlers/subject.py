from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from bot.buttons.inline import inline_crud_btn, subject_list_btn
from bot.buttons.reply import admin_menu_btn
from bot.buttons.text import subjects
from bot.state.main import SubjectState
from db.model import Subjects
from dispatcher import dp


@dp.message(lambda msg : msg.text == subjects)
async def subject_handler(msg : Message , state : FSMContext):
    await msg.answer_photo("https://telegra.ph/file/8306aeb3efa90a79e494e.png", reply_markup=ReplyKeyboardRemove())
    await state.set_state()
    await msg.answer("Subject CRUD" , reply_markup=inline_crud_btn('subject'))


@dp.callback_query(lambda call : call.data.startswith("back_"))
async def back_handler(call : CallbackQuery, state : FSMContext):
    await call.message.delete()
    await call.message.answer("Back" , reply_markup=admin_menu_btn())


@dp.callback_query(lambda call : call.data.endswith("_subject"))
async def crud_handler(call : CallbackQuery, state : FSMContext):

    method = call.data.split("_")[0]
    if method == "insert":
        await call.message.delete()
        await state.set_state(SubjectState.name)
        await call.message.answer("Subject name : ")

    if method == "delete":
        await state.set_state(SubjectState.delete)
        subjects = Subjects().select()
        await call.message.edit_text("Select Subject" , reply_markup=subject_list_btn(subjects))


@dp.callback_query(SubjectState.delete)
async def delete_subject_handler(call : CallbackQuery):
    if call.data == "back":
        await call.message.edit_text("Subject CRUD" , reply_markup=inline_crud_btn('subject'))
    else:
        sub_id = int(call.data.split("_")[1])
        Subjects(id = sub_id).delete()
        subjects = Subjects().select()
        await call.message.edit_reply_markup(reply_markup=subject_list_btn(subjects))



@dp.message(SubjectState.name)
async def sub_name_handler(msg : Message, state : FSMContext):
    Subjects(name = msg.text).insert()
    await state.clear()
    await msg.answer("Subject CRUD", reply_markup=inline_crud_btn('subject'))







