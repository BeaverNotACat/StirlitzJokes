from telebot.async_telebot import AsyncTeleBot
# from StirlitzJockes.jokes_parser import JokesParser
from StirlitzJockes.handlers import register_handlers
from StirlitzJockes.settings import BOT_TOKEN

# parser = JokesParser(JOKES_SOURSE_URL)

bot = AsyncTeleBot(BOT_TOKEN)
register_handlers(bot)
