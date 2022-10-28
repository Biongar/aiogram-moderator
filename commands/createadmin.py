from config.database.settings import database
from src.account.managers import UserManager


user_manager = UserManager()


async def create_admin():
    await database.connect()
    try:
        pk = int(input('Введите id пользователя в телеграм: '))
    except ValueError:
        print('id должно быть целым числом')
        await database.disconnect()
        return
    
    username = input('Введите username пользователя в телеграм: ')

    user = await user_manager.get_by_id(pk)

    if user and not user.is_admin:
        await user_manager.promote_user(user.id)
        print(f'{username} теперь администратор')

    elif user and user.is_admin:
        print('Пользователь уже является администратором')
        
    else:
        await user_manager.create({'id': pk, 'username': username})
        print(f'Пользователь {username} с id {pk} теперь администратор')
        
    await database.disconnect()


    
