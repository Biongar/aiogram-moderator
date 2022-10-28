from aiogram import types
from aiogram.dispatcher import FSMContext


from config.settings import dispatcher

from src.account.utils import auth, moderation
from src.account.managers import UserManager

from .utils import get_swear_words
from .commands.fsm_unban import register_handlers as register_unban_handlers
from .commands.fsm_ban import register_handlers as register_ban_handlers
from .commands.get_users import register_handlers as register_get_users_handlers

FORBIDDEN_WORDS = get_swear_words()
user_manager = UserManager()

@auth
async def command_start(message: types.Message):
    message_text = '''
*Доступные команды:*
/start \- Начало работы с ботом\.
/help \- Список доступных команд\.
/get_all_users \- Список пользователей в Базе Данных\.
/ban \- Забанить пользователя по id\.
/unban \- Разбанить пользователя по id\.
/cancel \- Отмена команды, которая выполняется в данный момент\.
'''
    await message.answer(message_text, parse_mode='MarkdownV2')
    
@moderation
async def bot_moderator(message: types.Message):
    message_text = 'Ругательства не разрешены в этом чате.'
    for word in message.text.lower().split(' '):
        if word in FORBIDDEN_WORDS:
            await user_manager.increase_violations(message['from']['id'])
            await message.answer(f'{message["from"]["username"]}! {message_text}')
            await message.delete()
    
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    
    await state.finish()
    await message.answer('Отменено')

def register_handlers():
    dispatcher.register_message_handler(command_start, commands=['start', 'help'])
    dispatcher.register_message_handler(cancel_handler, commands=['cancel'], state='*')
    register_unban_handlers()
    register_ban_handlers()
    register_get_users_handlers()
    dispatcher.register_message_handler(bot_moderator)
    