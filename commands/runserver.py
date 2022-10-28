from aiogram import executor

from config.settings import dispatcher
from config.database.settings import database
from src.handlers import register_project_handlers


async def startup(dispatcher):
    await database.connect()
    print('Бот онлайн')
    
async def shutdown(dispatcher):
    await database.disconnect()
    print('Бот офлайн')

def run_server():
    register_project_handlers()
    executor.start_polling(dispatcher, on_startup=startup, on_shutdown=shutdown)