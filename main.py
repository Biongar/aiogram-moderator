import asyncio
from sys import argv

from commands.commands_list import commands

def main():
    if len(argv) < 2:
        print('Список доступных комманд:')
        for command in commands:
            print(f'{command} - {commands[command]["description"]};')
            
    elif len(argv) > 2:
        print('Вы передали слишком много параметров.')
        
    elif argv[1] not in commands:
        print('Команда не найдена')
    
    else:
        command = argv[1]
        if commands[command]['type'] == 'async':
            asyncio.run(commands[command]['run_script']())
        else:
            commands[command]['run_script']()
            
            
if __name__ == '__main__':
    main()

