from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from dotenv import dotenv_values


env = dotenv_values('.env')

TOKEN = env.get('BOT_TOKEN')

storage = MemoryStorage()

bot = Bot(TOKEN)
dispatcher = Dispatcher(bot, storage=storage)

DATABASE_SETTINGS = {
    'NAME': env.get('DB_NAME'),
    'USER': env.get('DB_USER'),
    'PASSWORD': env.get('DB_PASSWORD'),
    'HOST': env.get('DB_HOST'),
}