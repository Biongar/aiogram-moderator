from aiogram import types

from config.settings import dispatcher
from src.account.utils import auth
from src.account.managers import UserManager


user_manager = UserManager()


@auth
async def get_users_command(message: types.Message):
    ''' TODO
    Изменить вывод, вместо простого сообщения отправлять сообщение "Список пользователей:",
    а к нему прикрепить кнопки с username пользователей(по 1 пользователю на кнопку), а в конце добавить
    2 кнопки (назад, вперед) для пагинации
    '''
    users_list = await user_manager.get_all_users(offset=0)
    message_text = '*Список пользователей:*\n'
    for user in users_list:
        message_text += f'id: {user.id}, username: {user.username}\n'
    await message.answer(message_text, parse_mode='MarkdownV2')
    
    
def register_handlers():
    dispatcher.register_message_handler(get_users_command, commands=['get_users'])