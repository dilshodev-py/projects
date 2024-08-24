from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, InputMediaPhoto, InlineQuery, InlineQueryResultArticle, \
    InputTextMessageContent
from aiogram.utils.i18n import lazy_gettext as __

from bot.buttons.inline import category_inline_button, product_inline_button
from bot.state import MenuState
from db.models import Product

menu_router = Router()


@menu_router.message(F.text == __('Menu'))
async def category_show_menu(message: Message, state: FSMContext):
    await state.set_state(MenuState.category)
    await message.answer_photo(photo="https://telegra.ph/file/1948eccc936367720ee16.png" , caption="Category menu", reply_markup=(await category_inline_button()))


@menu_router.callback_query(MenuState.category)
async def product_page_handler(callback: CallbackQuery, state: FSMContext):
    category_id = callback.data
    products: list[Product] = Product().select(category_id=int(category_id))
    await state.update_data({"category_id": category_id, "page_num": 0, "count": 0 , "products" : products})
    session_product = products[0]
    make_caption = "Name : {name}\nDescription : {description}\nPrice : {price}"

    await state.set_state(MenuState.pagination)
    photo = InputMediaPhoto(media = session_product.photo,caption=make_caption.format_map(session_product.__dict__))
    await callback.message.edit_media(media=photo,
                                        reply_markup=(await product_inline_button(0, 0))
                                        )

@menu_router.callback_query(MenuState.pagination , F.data.startswith("pagination_"))
async def pagination_handler(callback : CallbackQuery , state : FSMContext):
    page_num = int(callback.data.split("_")[-1])
    data = await state.get_data()
    session_product = data.get('products')[page_num]
    await state.update_data({"page_num": page_num})
    make_caption = "Name : {name}\nDescription : {description}\nPrice : {price}"
    photo = InputMediaPhoto(media=session_product.photo , caption=make_caption.format_map(session_product.__dict__))
    await callback.message.edit_media(photo,reply_markup=(await product_inline_button(page_num, 0)))


@menu_router.callback_query(MenuState.pagination , F.data == "back")
async def back_handler(callback : CallbackQuery , state : FSMContext):
    await state.set_state(MenuState.category)
    photo = InputMediaPhoto(media="https://telegra.ph/file/1948eccc936367720ee16.png" , caption="Category menu")
    await callback.message.edit_media( photo, reply_markup=(await category_inline_button()))



@menu_router.inline_query()
async def inline_query(inline : InlineQuery):
    print(inline.query)
    products = Product().filter_name(inline.query)
    result = []
    for product in products:
        result.append(
            InlineQueryResultArticle(
                id = str(product.id),
                title=product.name,
                description= product.description + f"\nPrice: {product.price}",
                thumbnail_url=product.photo,
                input_message_content=InputTextMessageContent(message_text=f"{product.id}")
            )
        )
    return inline.answer(result,cache_time=5, is_personal=True)
# name
# description
# price
#
# <-    ->
# -   0   +
#  delete🗑
#   order✅
# category menu
