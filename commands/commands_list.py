from .runserver import run_server
from .createadmin import create_admin


commands = {
    'runserver': {
        'run_script': run_server, 
        'type': 'sync', 
        'description': 'Старт бота'
        },
    'createadmin': {
        'run_script': create_admin, 
        'type': 'async', 
        'description': 'Добавление прав администратора пользователю'
        },
}