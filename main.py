import json
import commands as cmd

ps5_games = []
    
try:
    ps5_games = cmd.load()
    print(ps5_games)
except:
    print("Первый запуск или список игр пуст, добавьте игры в список!")

while True:
    command = input("Введите команду: ")
    if command == "!show_list":
        print(f'Вот текущий список игр {ps5_games}')
        
    elif command == "!find_game":
        cmd.find_game(ps5_games)    
        
    elif command == "!add_game":
        ps5_games.append(cmd.add_game())
        print("Запись по игре добавлена!")
    
    elif command == "!save":
        cmd.save(ps5_games) 
        print("Данные сохранены!")   
    
    elif command == "!delete_game":
        del ps5_games[cmd.delete_game(ps5_games)]
        print("Запись удалена!")
        
    elif command == "!redactor":
        chek_data = str(input(f"Введите Название игры: "))
        for i in range (0,len(ps5_games)):
            if ps5_games[i][0] == chek_data:
                break
        ps5_games[i] = cmd.redact(ps5_games[i])
        
    elif command == "!stop":
        while True:
            try:
                exit = input("Вы хотите сохранить изменения? (Да/Нет)")
                if exit == "Да":
                    cmd.save(ps5_games)
                    print("Изменения сохранены. До свидания!")
                elif exit == "Нет":
                    print("Данные после последнего сохранения будут утеряны. До свидания!")
            except:
                print("Введите корректную команду!")
            break
        break
    