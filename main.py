import time
import dotenv
import os
from telethon import TelegramClient
from telethon import sync, events
from telethon.errors.rpcerrorlist import ChannelPrivateError


dotenv.load_dotenv()
client = TelegramClient(os.getenv('BOT_NAME'), int(os.getenv('API_ID')), os.getenv('API_HASH'))
client.start(phone=str(os.getenv('PHONE_NUMBER')))
bos_name = os.getenv('BOSS_NAME')


def send_chat_list(client):
    chat_list = []
    dlgs = client.get_dialogs()
    for dlg in dlgs:
        chat_list.append(dlg.name)
    return chat_list


def get_usernames(client, chat_name):
    user_list = []
    usernames = client.get_participants(chat_name, aggressive=True)
    for username in usernames:
        user_list.append(username.username)
    return user_list


client.send_message(bos_name, str('Бот Активирован'))
while True:
    msg = client.get_messages(bos_name, limit=1)
    time.sleep(3)
    for mes in msg:
        if mes.message == '/chat':
            chat_list = send_chat_list(client)
            client.send_message(bos_name, str(chat_list))
        elif mes.message[0:6] == '/parse':
            chat_name = mes.message[7:]
            filename = chat_name.replace(' ', '_')
            filename = filename.replace('/', '_')
            dlgs = client.get_dialogs()
            if mes.message[0:11] == '/parse_week':
                print(mes.message[0:11])
                print('WORKS')
                user_list =[]
            else:
                try:
                    user_list = get_usernames(client, chat_name)
                except ValueError as e:
                    client.send_message(bos_name, "Проверь кривые руки, добавил ли ты чат, и правильно ли ты вставил название чата")
                    continue
                except ChannelPrivateError:
                    client.send_message(bos_name, 'Этот чат имеет приваные настройки доступа')
                    continue
            with open(f'{filename[0:6]}.txt', mode='a') as f:
                for user in user_list:
                    if user == 'None' or user is None:
                        continue
                    f.write(str(user) + '\n')
                f.close()
            print(f'Parsed: {filename[0:6]}')
            client.send_message(bos_name, 'Ready!')
            client.send_file(bos_name, file=f'{filename[0:6]}.txt')
        elif mes.message[0:6] == '/help':
            client.send_message(bos_name, 'Команды:\n'
                                          '/chat - выводит список чатов\n'
                                          '/parse <название чата> - парсит юзеров с чата\n'
                                          '/help - показывает команды бота'
                                          '/parse_week - парсит юзеров с чата активные за последнюю неделю\n')

