import telebot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

bot = telebot.TeleBot('7507461491:AAFIiHIUv_xR44kMYlVMNl264KvjLl0gJa4')
import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')
django.setup()
from apps.models import User


@bot.message_handler(commands=['start'])
def start(message):
    user = User.objects.first()
    bot.send_message(message.chat.id, f'{bot.bot_id}')


bot.infinity_polling()
