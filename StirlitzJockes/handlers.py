from telebot import types
from telebot.async_telebot import AsyncTeleBot
from StirlitzJockes.jokes_parser import JokesParser
from StirlitzJockes.settings import JOKES_SOURSE_URL
# from StirlitzJockes import parser

parser = JokesParser(JOKES_SOURSE_URL)


async def echo_handler(message: types.Message, bot: AsyncTeleBot):
    await bot.send_message(message.chat.id, 'pls use /joke')


async def command_handler(message: types.Message, bot: AsyncTeleBot):
    await bot.send_message(message.chat.id, parser.get_joke())


def register_handlers(bot: AsyncTeleBot):
    bot.register_message_handler(
        command_handler,
        func=lambda message: message.text == '/joke',
        pass_bot=True)
    bot.register_message_handler(echo_handler, pass_bot=True)
