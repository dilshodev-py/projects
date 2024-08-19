#
# @order_router.callback_query(F.data == 'confirm_order')
# async def command_start_handler(call: CallbackQuery, state: FSMContext) -> None:
#     data = await state.get_data()
#     order = await Order.by_user_get(user_id=call.from_user.id)
#     await call.message.delete()
#     prices = [
#         LabeledPrice(label=_('Price of products'), amount=data.get('total') * 100)
#     ]
#     await call.message.answer_invoice(_('Products'), data.get('text'), f'{order.id}', conf.bot.PAYMENT_CLICK_TOKEN,
#                                       'UZS', prices)
#
#
# @order_router.message(lambda message: bool(message.successful_payment))
# async def confirm_handler(message: Message, state: FSMContext):
#     if message.successful_payment:
#         total_amount = message.successful_payment.total_amount//100
#         order_id = int(message.successful_payment.invoice_payload)
#         await Order.update(id_=order_id, status=Order.OrderStatusEnum.APPROVED , total_amount = total_amount)
#         await message.answer(text="To'lo'vingiz uchun raxmat 😊", reply_markup=main_menu_btn())
#
#
# @order_router.pre_checkout_query()
# async def command_start_handler(pre_checkout_query: PreCheckoutQuery) -> None:
#     await pre_checkout_query.answer(True)
