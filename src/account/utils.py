from aiogram import types

from .managers import UserManager
from .models import UserModel


user_manager = UserManager()

async def get_or_create_user(message: types.Message) -> UserModel:
    user = await user_manager.get_by_id(message['from']['id'])
    
    if user:
        return user
    
    instance = {
        'id': message['from']['id'],
        'username': message['from']['username']
    }
    
    await user_manager.create(instance)
    
    user = await user_manager.get_by_id(message['from']['id'])
    return user
    

def auth(func):
    async def wrapper(message: types.Message):
        user = await user_manager.get_by_id(message['from']['id'])
        
        if not user:
            return await message.answer('Доступ запрещен.')
        
        if not user.is_admin:
            return await message.answer('Доступ запрещен.')
        
        return await func(message)
    return wrapper


def moderation(func):
    async def wrapper(message: types.Message):
        user = await get_or_create_user(message)
        
        if user.is_banned:
            return await message.delete()

        if user.rule_violations > 2 and not user.is_banned:
            await user_manager.ban_user(user.id)
            return await message.delete()
        
        return await func(message)
    return wrapper