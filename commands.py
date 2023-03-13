import json

dict_column = ["Название","Год","Жанр","Статус","Комментарий"]

def load ():
    with open("ps5_games.json","r",encoding="utf-8") as fh:
        ps5_games = json.load(fh)
    print("Список игр загружен")
    return ps5_games

def save (ps5_games):
    with open("ps5_games.json","w",encoding="utf-8") as fh:
        fh.write(json.dumps(ps5_games, ensure_ascii=False))
    print("Список игр к прохождению обновлен и сохранен в файле ps5_games.json")
    
def add_game():
    array = []
    for i in range(0,len(dict_column)):
        array.append(input(f'Введите {dict_column[i]}:'))
    return array

def find_game(game_list):
    place = dict_column.index(input(f"Осуществить поиск по {dict_column}: "))
    chek_data = str(input(f"Введите {dict_column[place]}: "))
    for i in range (0,len(game_list)):
        if game_list[i][place] == chek_data:
            print(game_list[i])
            
def delete_game (game_list):
    chek_data = str(input(f"Введите Название игры: "))
    for i in range (0,len(game_list)):
            if game_list[i][0] == chek_data:
                break
    return i

def redact (game_list):

    command = str(input("Что вы хотите изменить? "))

    if command == "все":
        for i in range (0,len(game_list)):
            game_list[i]=str(input(f"Введите {dict_column[i]} для изменения: "))
    elif command not in dict_column:
        print("Нет такого поля!")
    else :
        place = dict_column.index(command)
        game_list[place] = str(input(f'Введите изменения по {dict_column[place]} :'))
    return game_list