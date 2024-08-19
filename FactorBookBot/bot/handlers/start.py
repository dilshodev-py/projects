from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent, LabeledPrice, \
    PreCheckoutQuery
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __
from aiogram.utils.markdown import hbold
from sqlalchemy import select, insert
from sqlalchemy.sql.operators import ilike_op

from bot.buttons.inline import our_network_btn
from bot.buttons.reply import main_menu_btn
from bot.dispatcher import dp
from db.models import User, session, Book, Contact

router = Router()

# PAYMENT_CLICK_TOKEN = "398062629:TEST:999999999_F91D8F69C042267444B74CC0B3C747757EB0E065"
# @router.message(F.text=="invoice")
# async def command_start_handler(msg: Message, state: FSMContext) -> None:
#     price = [LabeledPrice(label='product1' , amount=10000*100) ,
#              LabeledPrice(label='product2' , amount=100000*100)]
#     await msg.answer_invoice(_('Products'), "Product about", '10', PAYMENT_CLICK_TOKEN,
#                                       'UZS', price)

# @router.message(lambda message: bool(message.successful_payment))
# async def confirm_handler(message: Message, state: FSMContext):
#     if message.successful_payment:
#         total_amount = message.successful_payment.total_amount//100
#         order_id = int(message.successful_payment.invoice_payload)
#         print(total_amount)
#         print(order_id)
#         # await Order.update(id_=order_id, status=Order.OrderStatusEnum.APPROVED , total_amount = total_amount)
#         await message.answer(text="To'lo'vingiz uchun raxmat 😊", reply_markup=main_menu_btn())
#
#
# @router.pre_checkout_query()
# async def command_start_handler(pre_checkout_query: PreCheckoutQuery) -> None:
#     print('Tolov boshlanishi')
#     print(pre_checkout_query.invoice_payload)
#     print(pre_checkout_query.order_info)
#     await pre_checkout_query.answer(True)



@router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    query = select(User).where(User.chat_id == message.from_user.id)
    user = session.execute(query).fetchone()
    if not user:
        user = {
            "chat_id": message.from_user.id,
            "username": message.from_user.username,
            "fullname": message.from_user.full_name
        }
        query = insert(User).values(**user)
        session.execute(query)
        session.commit()

    await message.answer(_("Hello ") + f"{hbold(message.from_user.full_name)}!", parse_mode=ParseMode.HTML,
                         reply_markup=main_menu_btn())


@router.message(F.text == __("🔵 Our Network"))
async def our_network_handler(msg: Message):
    await msg.answer(text=_("🔵 Our Network"), reply_markup=our_network_btn())


@router.message(F.text == __("📞 Contact us"))
async def our_network_handler(msg: Message):
    contact: Contact = session.execute(select(Contact)).scalar()
    text = f"""
    Telegram: {contact.bot_link}

📞 {contact.phone_number}

🤖 Bot P20 guruhi (@Dilshod_Absaitov) tomonidan tayyorlandi.
    """
    await msg.answer(text=text)

@router.inline_query()
async def show_product(inline_query: InlineQuery):
    books: list[Book] = session.execute(select(Book).filter(ilike_op(Book.title, f"%{inline_query.query}%"))).scalars()
    result = [
        InlineQueryResultArticle(
            id=str(book.id),
            title=book.title,
            description=str(f"P20 books\n💴 Narxi: {book.price} so'm"),
            thumbnail_url=book.photo,
            input_message_content=InputTextMessageContent(message_text=book.title)
        )
        for book in books]
    await inline_query.answer(result, cache_time=5, is_personal=True)
