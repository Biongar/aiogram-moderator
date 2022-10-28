from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from config.settings import dispatcher

from src.account.utils import auth
from src.account.managers import UserManager


user_manager = UserManager()


class FSMUnban(StatesGroup):
    get_id = State()


@auth
async def unban_user_command(message: types.Message):
    await FSMUnban.get_id.set()
    await message.answer('Введите id пользователя')
    
    
async def get_id(message: types.Message, state: FSMContext):
    # async with state.proxy() as data:
    try: 
        user = await user_manager.get_by_id(int(message.text))
        
        if user:
            await user_manager.unban_user(user.id)
            await message.answer(f'Пользователь {user.username} разбанен')
        else:
            await message.answer('Пользователя с таким id не существует, повторите попытку')
            return
        
        await state.finish()
        
    except ValueError:
        await message.answer('id пользователя должен быть числовым значением, повторите попытку')


def register_handlers():
    dispatcher.register_message_handler(unban_user_command, commands=['unban'])
    dispatcher.register_message_handler(get_id, state=FSMUnban.get_id)
